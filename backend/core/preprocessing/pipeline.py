# Python
from __future__ import annotations
from pathlib import Path
# Bundle
import joblib
# Typing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sklearn.compose import ColumnTransformer

_LOCATION = Path(__file__).parent.parent.parent / 'research/core/preprocessing/pipeline.joblib'
assert _LOCATION.exists()

PIPELINE: 'ColumnTransformer' = joblib.load(_LOCATION)

