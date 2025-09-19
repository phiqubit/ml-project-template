PROJECT_NAME?=ml-project-template
IMAGE?=$(REGISTRY):latest
PY=python

.PHONY: setup lint test fmt pre-commit-install api docker-build docker-run docker-push k8s-apply k8s-delete dvc-pull dvc-push train predict docs

setup:
	$(PY) -m pip install --upgrade pip
	pip install -r requirements.txt
	pre-commit install

lint:
	ruff check src tests
	black --check src tests
	isort --check-only src tests

fmt:
	black src tests
	isort src tests

test:
	pytest -q --maxfail=1 --disable-warnings

api:
	uvicorn src.api:app --host 0.0.0.0 --port 8000

train:
	$(PY) -m src.models.train

predict:
	$(PY) -m src.models.predict --input sample.json

docker-build:
	docker build -t $(IMAGE) .

docker-run:
	docker run --rm -p 8000:8000 --env-file .env $(IMAGE)

docker-push:
	docker push $(IMAGE)

k8s-apply:
	kubectl apply -f k8s/

k8s-delete:
	kubectl delete -f k8s/ || true

dvc-pull:
	dvc pull

dvc-push:
	dvc push

docs:
	pdoc --html src --output-dir docs --force

