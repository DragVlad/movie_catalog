from api import router as api_router

from fastapi import (
    FastAPI,
    Request,
)


app = FastAPI(
    title="Movie Catalog Api",
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
