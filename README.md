# fastapi-blueprint

## Setup the environment

### Requirements

- Poetry

### Installing dependencies

```
poetry install
poetry run pre-commit install
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

## Migrations

### Create a new migration

```
poetry run alembic revision --autogenerate -m "message"
```

### Apply migrations

```
poetry run alembic upgrade head
```

## Features to be included

- [ ] Docker compose structure
- [x] Poetry
- [x] REST API
- [x] DB connection
- [x] Alembic migrations
- [x] GraphQL API
- [ ] Celery async tasks
- [ ] Admin interface
- [x] Tests
- [x] Coverage
- [ ] CI/CD pipeline
- [ ] Monitoring
- [ ] Logging
- [ ] Error handling
- [ ] Rate limiting
- [ ] Caching
- [ ] Email sending
- [ ] File storage
