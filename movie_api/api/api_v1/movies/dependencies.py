import logging

from .crud import storage
from schemas.movies import Movie

from fastapi import (
    HTTPException,
    BackgroundTasks,
    Request,
    status,
)


log = logging.getLogger(__name__)


UNSAVE_METHODS = frozenset(
    {
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
    }
)


def found_movie(
    slug: str,
) -> Movie | None:
    movie: Movie | None = storage.get_movie_by_slug(slug=slug)
    if movie:
        return movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie {slug!r} not found",
    )


def save_storage_state(
    request: Request,
    background_tasks: BackgroundTasks,
):
    yield
    if request.method in UNSAVE_METHODS:
        log.info("Add background task to save movie storage")
        background_tasks.add_task(storage.save_state)
