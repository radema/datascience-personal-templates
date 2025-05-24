# tests/test_main.py
from pathlib import Path
import sys

# Ensure src is importable whether tests are run from the project root or template root
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def test_main_runs():
    from src.main import main
    assert main() is None  # or your actual expected behavior
