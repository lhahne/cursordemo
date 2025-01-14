"""Time-related endpoints router."""
from datetime import datetime

import pytz
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter(tags=["time"])


@router.get("/datetime")
async def get_datetime(timezone: str = "UTC") -> JSONResponse:
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
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid timezone",
                "message": f"Timezone '{timezone}' not found. Please use a valid timezone name (e.g., 'UTC', 'Europe/London', 'America/New_York')."
            }
        ) 