import unittest
import threading
import time
import requests
import json
from brain_server import run_server

class TestPayloadLimit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start server in a separate thread
        cls.port = 8002
        cls.server_thread = threading.Thread(target=run_server, args=(cls.port,))
        cls.server_thread.daemon = True
        cls.server_thread.start()
        # Give server a moment to start
        time.sleep(2)

    def test_payload_too_large(self):
        # Send >1MB payload
        url = f"http://localhost:{self.port}/api/audit"
        headers = {'Content-Type': 'application/json'}
        large_payload = '{"question": "' + 'A' * 1048576 + '", "user_doubt": "doubt"}'
        response = requests.post(url, headers=headers, data=large_payload)

        self.assertEqual(response.status_code, 413)
        self.assertEqual(response.json()["message"], "Invalid Payload Size")


    def test_valid_payload(self):
        # Send valid payload
        url = f"http://localhost:{self.port}/api/audit"
        headers = {'Content-Type': 'application/json'}
        valid_payload = json.dumps({"question": "Test question?", "user_doubt": "Test doubt"})
        response = requests.post(url, headers=headers, data=valid_payload)

        self.assertEqual(response.status_code, 200)

    def test_negative_content_length_raw(self):
        import socket
        host = 'localhost'
        port = self.port
        request = (
            "POST /api/audit HTTP/1.1\r\n"
            f"Host: localhost:{port}\r\n"
            "Content-Length: -1\r\n"
            "Content-Type: application/json\r\n"
            "Connection: close\r\n"
            "\r\n"
            "{\"question\": \"test\"}"
        )
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendall(request.encode('utf-8'))
        response = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data
        s.close()

        # BaseHTTPRequestHandler doesn't easily let us send 413 the normal way with self.send_response
        # when we also send a JSON body. The response raw has "413" inside it though from the socket test
        self.assertIn(b"413", response)
        self.assertIn(b"Invalid Payload Size", response)

if __name__ == '__main__':
    unittest.main()
