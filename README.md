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

## Execute as docker compose

```
docker compose build
docker compose up
```

Using this commands you will start multiple docker containers and will serve the API at port 8080 and the flower (celery monitoring page) at port 5555

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

- [x] Docker compose structure
- [x] Poetry
- [x] REST API
- [x] DB connection
- [x] Alembic migrations
- [x] GraphQL API
- [x] Celery async tasks
- [x] Admin interface
- [x] Tests
- [x] Coverage
- [ ] Caching
- [ ] Logging
- [ ] Monitoring
- [ ] Error handling
- [ ] Rate limiting
- [ ] Email sending
