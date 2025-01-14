"""Root endpoints router."""
from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/")
async def read_root() -> FileResponse:
    """Serve the index.html page."""
    return FileResponse("app/static/index.html") 