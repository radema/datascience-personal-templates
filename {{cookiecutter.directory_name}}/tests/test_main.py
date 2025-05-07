"""Unit tests for the main module."""
import sys

sys.path.append("../src")  # Adjust the path to your src directory


def test_main_runs():
    """Test if the main function runs without errors."""
    from main import main

    assert main() is None  # or your actual expected behavior
