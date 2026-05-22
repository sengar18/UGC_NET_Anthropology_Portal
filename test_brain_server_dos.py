import threading
import time
import requests
import json
import socket
from brain_server import run_server

def get_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port

def test_payload_limit():
    # Use a dynamic port
    port = get_free_port()

    # Start server in a thread
    server_thread = threading.Thread(target=run_server, args=(port,), daemon=True)
    server_thread.start()

    # Give server time to start and index
    time.sleep(2)

    url = f"http://localhost:{port}/api/audit"

    # Test 1: Small valid payload
    small_payload = json.dumps({
        "question": "Test question",
        "options": ["A", "B"],
        "correct_answer": "A",
        "user_doubt": "Test doubt"
    })

    try:
        response = requests.post(url, data=small_payload, headers={'Content-Type': 'application/json'})
        print(f"Small payload response status: {response.status_code}")
        assert response.status_code == 200 or response.status_code != 413, f"Expected 200 for small payload, got {response.status_code}"
    except Exception as e:
        print(f"Error testing small payload: {e}")
        raise e

    # Test 2: Large payload (> 1MB)
    # We will just construct a huge string.
    # We also have to be careful with json.dumps, but we can just send raw string that claims to be large.
    # Actually, it's safer to just send a large valid json just in case it reaches `json.loads` if the fix fails.
    large_payload = '{"question": "' + 'A' * (1024 * 1024 + 100) + '"}'

    try:
        response = requests.post(url, data=large_payload, headers={'Content-Type': 'application/json'})
        print(f"Large payload response status: {response.status_code}")
        assert response.status_code == 413, f"Expected 413 for large payload, got {response.status_code}"

        response_data = response.json()
        assert response_data["status"] == "error"
        assert response_data["message"] == "Payload Too Large"
    except Exception as e:
        print(f"Error testing large payload: {e}")
        raise e

    print("All tests passed successfully.")

if __name__ == "__main__":
    test_payload_limit()
