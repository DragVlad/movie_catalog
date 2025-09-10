from fastapi import APIRouter

from .movies.views import router as movies_router

router = APIRouter(
    prefix="/v1",
)
router.include_router(movies_router)
