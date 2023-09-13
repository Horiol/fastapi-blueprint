# fastapi-blueprint

## Setup the environment

### Requirements

- Poetry

### Installing dependencies

```
poetry install
poetry run pre-commit install --hook-type commit-msg --hook-type prepare-commit-msg --hook-type pre-commit --hook-type pre-push
```

## Run in development

```
poetry run python src/main.py
```

## Execute test suite

```
poetry run pytest --cov=src --cov-context=test --cov-branch --cov-report xml --cov-report term
```

## Execute as production

```
poetry run uvicorn src.main:app
```
