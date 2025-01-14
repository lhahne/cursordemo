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
├── .gitignore           # Git ignore rules
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
├── ruff.toml           # Ruff linter configuration
├── pytest.ini          # Pytest configuration
└── run.py              # Application entry point
```

## Setup

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

Run the tests using pytest:
```bash
pytest
```

This will run all tests with verbose output. The test suite includes:
- Endpoint testing
- Static file serving
- API documentation availability

## Code Quality

The project uses Ruff for linting. Run the linter with:
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

4. **API Design**
   - RESTful principles
   - Clear error handling
   - Comprehensive documentation
   - Type-safe responses 