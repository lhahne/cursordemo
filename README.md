# FastAPI Web Service

A simple web service built with FastAPI, uvicorn, and Tailwind CSS.

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
python main.py
```

Or with uvicorn directly:
```bash
uvicorn main:app --reload
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

## Access the Application

- Web Interface: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative API Documentation: http://localhost:8000/redoc

## Project Structure

- `main.py` - FastAPI application
- `static/` - Static files directory
  - `index.html` - Main webpage with Tailwind CSS
- `requirements.txt` - Python dependencies
- `venv/` - Virtual environment (don't commit this)
- `tests/` - Test suite
  - `test_main.py` - Main application tests
- `pytest.ini` - Pytest configuration
- `.github/workflows/` - GitHub Actions CI configuration
- `ruff.toml` - Ruff linter configuration 