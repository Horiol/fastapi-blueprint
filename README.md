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
poetry run uvicorn src.main:app --reload
```

## Execute test suite

```
poetry run pytest --cov=src --cov-context=test --cov-branch --cov-report xml --cov-report term
```

## Execute as production

```
poetry run uvicorn src.main:app
```

## Features to be included

- [ ] Docker compose structure
- [ ] DB connection
- [ ] Alembic migrations
- [ ] Celery async tasks
