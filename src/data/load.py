"""
Data loading utilities.

Note:
Replace the placeholder functions with your actual data sources (CSV, Parquet, DB, etc.)
and wire them into the DVC pipeline.
"""
from pathlib import Path
import pandas as pd

def load_csv(path: str | Path) -> pd.DataFrame:
    """Load a CSV into a DataFrame."""
    return pd.read_csv(path)

