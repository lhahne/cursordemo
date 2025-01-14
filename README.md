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