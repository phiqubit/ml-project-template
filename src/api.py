"""
FastAPI inference service.

Endpoints
---------
GET /health         -> simple health check
POST /predict       -> run model inference on numeric feature list
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
import joblib
import os
from typing import Optional

app = FastAPI(title="ML API", version="0.1.0")

class Features(BaseModel):
    """Payload schema for prediction."""
    values: conlist(float, min_items=1)  # list[float] with at least 1 item

_MODEL = None
MODEL_PATH = os.getenv("MODEL_PATH", "models/model.pkl")

@app.get("/health")
def health() -> dict:
    """Kubernetes-ready liveness/readiness endpoint."""
    return {"status": "ok"}

def _load_model(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found at {path}. Train and save the model first.")
    return joblib.load(path)

@app.post("/predict")
def predict(payload: Features) -> dict:
    """
    Run model inference on a vector of floats.

    Parameters
    ----------
    payload : Features
        JSON payload with `values: List[float]`.

    Returns
    -------
    dict : {"prediction": float}
    """
    global _MODEL
    try:
        if _MODEL is None:
            _MODEL = _load_model(MODEL_PATH)
        pred = _MODEL.predict([payload.values])[0]
        return {"prediction": float(pred)}
    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {e}")
