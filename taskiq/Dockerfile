# Use Python 3.11 slim as the base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Create a non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Install poetry
RUN pip install poetry
RUN poetry self add poetry-plugin-export

# Copy application code
COPY pyproject.toml poetry.lock ./


# Install dependencies
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt 

# Copy the rest of the application code
COPY ./src ./src

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Run celery worker with flower
CMD ["taskiq", "worker", "src.worker:broker"]

