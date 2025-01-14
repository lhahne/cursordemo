"""Main application module."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import root_router, time_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="FastAPI Web Service",
        description="A simple web service with time and static file serving capabilities",
        version="1.0.0",
    )

    # Mount static files
    app.mount("/static", StaticFiles(directory="app/static"), name="static")

    # Include routers
    app.include_router(root_router.router)
    app.include_router(time_router.router, prefix="/api")

    return app


# Create the application instance
app = create_app() 