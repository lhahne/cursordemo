from fastapi.testclient import TestClient
from main import app
import json
from datetime import datetime
import pytz

client = TestClient(app)

def test_read_root():
    """Test the root endpoint returns the index.html file."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "<title>FastAPI Web Service</title>" in response.text

def test_static_files():
    """Test that static files are being served."""
    response = client.get("/static/index.html")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "<title>FastAPI Web Service</title>" in response.text

def test_docs_available():
    """Test that API documentation is accessible."""
    response = client.get("/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "swagger" in response.text.lower()

def test_redoc_available():
    """Test that ReDoc documentation is accessible."""
    response = client.get("/redoc")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "redoc" in response.text.lower()

def test_get_datetime_default():
    """Test getting datetime with default timezone (UTC)."""
    response = client.get("/api/datetime")
    assert response.status_code == 200
    data = response.json()
    assert data["timezone"] == "UTC"
    # Verify the response contains all required fields
    assert all(key in data for key in ["datetime", "date", "time", "timezone", "timezone_offset", "day_of_week"])
    
def test_get_datetime_specific_timezone():
    """Test getting datetime for a specific timezone."""
    timezone = "Europe/London"
    response = client.get(f"/api/datetime?timezone={timezone}")
    assert response.status_code == 200
    data = response.json()
    assert data["timezone"] == timezone
    
def test_get_datetime_invalid_timezone():
    """Test getting datetime with invalid timezone."""
    response = client.get("/api/datetime?timezone=Invalid/Timezone")
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    assert data["error"] == "Invalid timezone" 