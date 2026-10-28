"""Put the lab folder on sys.path so the tests can import transit.

pytest imports conftest.py before collecting the sibling test files, so
the insertion below is in place by the time test_lab07.py runs
``from transit import ...``.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
