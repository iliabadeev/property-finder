# Python
from __future__ import annotations
from pathlib import Path
# Bundle
import joblib


_LOCATION = Path(__file__).parent.parent.parent / 'research/core/models/transacted.joblib'
assert _LOCATION.exists()

MODEL_TRANSACTED = joblib.load(_LOCATION)
