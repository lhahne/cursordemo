# FastAPI Web Service

A simple web service built with FastAPI, uvicorn, and Tailwind CSS.

## Project Structure

```
.
├── app/                    # Application package
│   ├── __init__.py        # Package initialization
│   ├── main.py            # Application factory and configuration
│   ├── routers/           # API route handlers
│   │   ├── __init__.py
│   │   ├── root_router.py # Root endpoint handlers
│   │   └── time_router.py # Time-related endpoint handlers
│   └── static/            # Static files
│       └── index.html     # Main webpage
├── tests/                 # Test suite
│   └── test_app.py       # Application tests
├── .github/              # GitHub configuration
│   └── workflows/        # GitHub Actions workflows
├── .dockerignore        # Docker ignore rules
├── .gitignore           # Git ignore rules
├── Dockerfile           # Docker image definition
├── README.md            # Project documentation
├── docker-compose.yml   # Docker Compose configuration
├── requirements.txt     # Python dependencies
├── ruff.toml           # Ruff linter configuration
├── pytest.ini          # Pytest configuration
└── run.py              # Application entry point
```

## Setup

### Using Docker (Recommended)

1. Build and start the container:
```bash
docker compose up --build
```

The application will be available at http://localhost:8000

To run in detached mode:
```bash
docker compose up -d
```

To stop the container:
```bash
docker compose down
```

### Manual Setup

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python run.py
```

## Testing

### With Docker

```bash
docker compose exec web pytest
```

### Without Docker

```bash
pytest
```

This will run all tests with verbose output. The test suite includes:
- Endpoint testing
- Static file serving
- API documentation availability

## Code Quality

### With Docker

```bash
docker compose exec web ruff check .
```

To automatically fix issues:
```bash
docker compose exec web ruff check --fix .
```

### Without Docker

```bash
ruff check .
```

To automatically fix issues:
```bash
ruff check --fix .
```

## Continuous Integration

GitHub Actions automatically runs the following checks on all pull requests and pushes to main:
- Tests on Python 3.11, 3.12, and 3.13
- Linting with Ruff
- Code style verification
- Docker build verification

## API Documentation

- Web Interface: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative API Documentation: http://localhost:8000/redoc

## Features

- Local time display with automatic timezone detection
- RESTful API endpoints for time information
- Modern UI with Tailwind CSS
- Comprehensive test suite
- Continuous Integration with GitHub Actions
- Code quality enforcement with Ruff
- Docker support for easy deployment

## Best Practices

This project follows several Python and FastAPI best practices:

1. **Project Structure**
   - Modular package organization
   - Separation of concerns (routers, static files)
   - Clear entry points

2. **Code Quality**
   - Type hints
   - Docstrings
   - Linting with Ruff
   - Automated testing

3. **Development Workflow**
   - Virtual environment management
   - Dependency management
   - Continuous Integration
   - Code quality gates
   - Docker containerization

4. **API Design**
   - RESTful principles
   - Clear error handling
   - Comprehensive documentation
   - Type-safe responses

## Docker Configuration

The project includes a production-ready Docker setup with:

1. **Multi-stage builds** for optimal image size
2. **Health checks** for container monitoring
3. **Volume mounting** for development
4. **Environment variable** support
5. **Security best practices**:
   - Non-root user
   - Minimal base image
   - No unnecessary dependencies 