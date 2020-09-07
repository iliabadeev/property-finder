# Python
from __future__ import annotations
from pathlib import Path
# Bundle
import joblib


_LOCATION = Path(__file__).parent.parent.parent / 'research/core/models/avm.joblib'
assert _LOCATION.exists()

MODEL_AVM = joblib.load(_LOCATION)
