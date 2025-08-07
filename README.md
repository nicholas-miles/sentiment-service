# Sentiment Analysis Service

A production-ready microservice for sentiment analysis using FastAPI and scikit-learn.

## Features

- **Sentiment Analysis**: 5-level sentiment classification (very negative, negative, neutral, positive, very positive)
- **FastAPI**: Modern, fast web framework with automatic API documentation
- **MLflow**: Model tracking and experiment management
- **Code Quality**: Black formatting and Ruff linting with pre-commit hooks
- **CI/CD**: Automated testing and quality checks on GitHub Actions

## Quick Start

### Prerequisites

- Python 3.12+ and Poetry, OR
- Docker and Docker Compose

### Option 1: Local Development

```bash
# Clone the repository
git clone <your-repo-url>
cd sentiment-service

# Install dependencies
poetry install

# Train the model
poetry run python src/sentiment_service/training/train.py

# Start the API server
poetry run uvicorn sentiment_service.api.main:app --reload
```

### Option 2: Docker

```bash
# Clone the repository
git clone <your-repo-url>
cd sentiment-service

# Build and run with Docker Compose
docker-compose up --build

# Or build and run manually
docker build -t sentiment-service .
docker run -p 8000:8000 sentiment-service
```

### API Usage

The API will be available at `http://localhost:8000`

- **Interactive docs**: `http://localhost:8000/docs`
- **Health check**: `GET /health`
- **Sentiment analysis**: `POST /predict`

Example request:
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie is absolutely fantastic!"}'
```

Example response:
```json
{
  "prediction": "very positive",
  "score": 0.435
}
```

## Development

### Code Quality

This project uses pre-commit hooks for code quality:

- **Black**: Code formatting
- **Ruff**: Linting and import sorting

The hooks run automatically on commit, or manually:

```bash
poetry run pre-commit run --all-files
```

### Docker Development

For consistent development environments, you can use Docker:

```bash
# Build the image
docker build -t sentiment-service .

# Run with volume mounting for development
docker run -p 8000:8000 -v $(pwd)/src:/app/src sentiment-service

# Or use docker-compose for easier management
docker-compose up --build
```

### Project Structure

```
sentiment-service/
├── src/sentiment_service/
│   ├── api/           # FastAPI application
│   ├── training/      # Model training scripts
│   └── models/        # Trained models
├── .github/workflows/ # CI/CD workflows
└── pyproject.toml     # Project configuration
```

## License

[Your License Here]
