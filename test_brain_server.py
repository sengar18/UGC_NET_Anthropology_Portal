import sys
import unittest
from unittest.mock import patch, MagicMock

import brain_server

class TestBrainServer(unittest.TestCase):

    @patch("brain_server.subprocess.run")
    @patch("builtins.__import__")
    def test_ensure_package_installation_failure(self, mock_import, mock_run):
        # Setup mock: __import__ fails
        mock_import.side_effect = ImportError("No module named 'dummy_import'")

        # Setup mock for subprocess.run to fail
        mock_run.return_value = MagicMock(returncode=1, stderr="pip error output")

        # Call function and expect exception
        with self.assertRaises(RuntimeError) as context:
            brain_server.ensure_package("dummy_package", "dummy_import")

        self.assertIn("Failed to install dummy_package:", str(context.exception))
        self.assertIn("pip error output", str(context.exception))

        # Verify subprocess.run was called
        mock_run.assert_called_once_with(
            [sys.executable, "-m", "pip", "install", "dummy_package"],
            capture_output=True, text=True
        )

if __name__ == '__main__':
    unittest.main()
