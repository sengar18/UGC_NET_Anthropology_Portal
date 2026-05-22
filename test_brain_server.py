import os
import pytest
from brain_server import safe_path

def test_safe_path_valid(tmp_path):
    # Setup a dummy directory and file
    base_dir = tmp_path / "base"
    base_dir.mkdir()
    target_file = base_dir / "target.txt"
    target_file.touch()

    # Get the real paths
    real_base = os.path.realpath(str(base_dir))
    real_target = os.path.realpath(str(target_file))

    # Should return the real path
    assert safe_path(str(target_file), str(base_dir)) == real_target

def test_safe_path_escape_relative(tmp_path):
    base_dir = tmp_path / "base"
    base_dir.mkdir()
    escape_file = tmp_path / "escape.txt"
    escape_file.touch()

    # Path traversal attempt
    relative_escape = os.path.join(str(base_dir), "..", "escape.txt")

    with pytest.raises(ValueError, match=f"Path escape blocked: .*"):
        safe_path(relative_escape, str(base_dir))

def test_safe_path_escape_absolute(tmp_path):
    base_dir = tmp_path / "base"
    base_dir.mkdir()
    escape_file = tmp_path / "escape.txt"
    escape_file.touch()

    # Absolute path outside base directory
    with pytest.raises(ValueError, match=f"Path escape blocked: .*"):
        safe_path(str(escape_file), str(base_dir))
