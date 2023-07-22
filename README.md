# fastapi-blueprint

## Setup the environment

### Requirements

- Poetry

### Installing dependencies

```
poetry install
poetry run pre-commit install --hook-type pre-commit --hook-type pre-push --hook-type commit-msg
```

## Run in development

```
poetry run python src/main.py
```

## Execute test suite

```
poetry run pytest --cov=src
```

## Execute as production

```
poetry run uvicorn src.main:app
```
