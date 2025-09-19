"""
Training script using Hydra for configuration and MLflow for tracking.

CLI examples
------------
python -m src.models.train
python -m src.models.train model.n_estimators=500 model.max_depth=12
"""

import os
import joblib
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.datasets import load_boston  # NOTE: placeholder; replace in production
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

import hydra
from omegaconf import DictConfig

@hydra.main(config_path='../../configs', config_name='config.yaml', version_base='1.2')
def main(cfg: DictConfig) -> None:
    """
    Train a RandomForest model and log metrics/artifacts to MLflow.

    Hydra config schema
    -------------------
    experiment_name: str
    model.n_estimators: int
    model.max_depth: int
    paths.model_path: str
    mlflow.tracking_uri: str | ''
    """
    # Configure MLflow
    mlflow.set_experiment(cfg.experiment_name)
    if cfg.mlflow.tracking_uri:
        mlflow.set_tracking_uri(cfg.mlflow.tracking_uri)

    # Placeholder dataset (replace with real data pipeline)
    data = load_boston()
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(
        n_estimators=int(cfg.model.n_estimators),
        max_depth=int(cfg.model.max_depth),
        random_state=42
    )

    with mlflow.start_run():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        r2 = r2_score(y_test, preds)

        mlflow.log_params({"n_estimators": cfg.model.n_estimators, "max_depth": cfg.model.max_depth})
        mlflow.log_metric("r2", float(r2))

        # Persist model
        os.makedirs(os.path.dirname(cfg.paths.model_path), exist_ok=True)
        joblib.dump(model, cfg.paths.model_path)
        mlflow.log_artifact(cfg.paths.model_path)

        print(f"R²: {r2:.4f} | Model saved -> {cfg.paths.model_path}")

if __name__ == "__main__":
    main()

