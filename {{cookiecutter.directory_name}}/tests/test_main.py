"""Unit tests for the main module."""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))


def test_main_runs():
    """Test if the main function runs without errors."""
    from main import main

    assert main() is None  # or your actual expected behavior
