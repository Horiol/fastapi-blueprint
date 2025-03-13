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
COPY . .

# Install dependencies
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt 

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port for the FastAPI server
EXPOSE 8000

# Run uvicorn server
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

