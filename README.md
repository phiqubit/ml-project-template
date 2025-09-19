# ML Project Template (Prod-Ready)

[![CI](https://github.com/phiqubit/ml-project-template/actions/workflows/ci.yml/badge.svg)](https://github.com/<your-username>/<repo-name>/actions/workflows/ci.yml)
[![Docker](https://github.com/phiqubit/ml-project-template/actions/workflows/docker.yml/badge.svg)](https://github.com/<your-username>/<repo-name>/actions/workflows/docker.yml)
[![Docs](https://img.shields.io/badge/docs-pdoc-blue.svg)](https://phiqubit.github.io/ml-project-template/)

One-command start for ML/DL projects with **Docker, K8s, FastAPI, Hydra, DVC, MLflow, and CI/CD**.

---

## Quickstart
1. Clone and create venv → `pip install -r requirements.txt`  
2. `pre-commit install`  
3. `dvc init` (+ add remote)  
4. `cp .env.example .env` and adjust  
5. `dvc repro` or `python -m src.models.train`  
6. `uvicorn src.api:app --reload`  

---

## Deploy
- **Docker**: `make docker-build && make docker-run`  
- **K8s**: set `REGISTRY`, update `k8s/deployment.yaml`, then `make k8s-apply`  

---

## CI/CD
- CI runs lint + tests on PRs  
- Docker workflow builds & pushes image on `main`/tags  
- CD applies manifests on successful image build  
- **Docs auto-published** at [Project Docs](https://phiqubit.github.io/ml-project-template/)  

---

## Documentation
The latest API & code documentation is available here:  
[Project Docs](https://phiqubit.github.io/ml-project-template/)
