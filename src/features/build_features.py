"""
Feature engineering building blocks.

Add your transforms here and call them from training/evaluation scripts.
"""
import pandas as pd

def add_bias(df: pd.DataFrame) -> pd.DataFrame:
    """Example: add a constant bias feature."""
    df = df.copy()
    df["bias"] = 1.0
    return df

