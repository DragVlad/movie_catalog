import logging

from api import router as api_router
from app_lifespan import lifespan
from core import config

from fastapi import (
    FastAPI,
    Request,
)

logging.basicConfig(
    level=config.LOG_LEVEL,
    format=config.LOG_FORMAT,
)


app = FastAPI(
    title="Movie Catalog Api",
    lifespan=lifespan,
)
app.include_router(api_router)


@app.get(
    "/",
    tags=["Root API"],
)
def read_root(
    request: Request,
):
    docs_url = request.url.replace(
        path="/docs",
    )
    return {
        "docs": str(docs_url),
    }
