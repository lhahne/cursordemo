from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from datetime import datetime
import pytz
import uvicorn

app = FastAPI(title="FastAPI Web Service")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

@app.get("/api/datetime")
async def get_datetime(timezone: str = "UTC"):
    """Get current date and time for the specified timezone."""
    try:
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz)
        
        return JSONResponse({
            "datetime": current_time.isoformat(),
            "date": current_time.date().isoformat(),
            "time": current_time.time().isoformat(),
            "timezone": timezone,
            "timezone_offset": current_time.strftime("%z"),
            "day_of_week": current_time.strftime("%A")
        })
    except pytz.exceptions.UnknownTimeZoneError:
        return JSONResponse(
            status_code=400,
            content={
                "error": "Invalid timezone",
                "message": f"Timezone '{timezone}' not found. Please use a valid timezone name (e.g., 'UTC', 'Europe/London', 'America/New_York')."
            }
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 