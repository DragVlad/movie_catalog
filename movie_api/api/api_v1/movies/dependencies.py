from .crud import MOVIES
from schemas.movies import Movie

from fastapi import (
    HTTPException,
    status,
)


def found_movie(
    slug: str,
) -> Movie | None:
    movie: Movie | None = next(
        (movie for movie in MOVIES if movie.slug == slug),
        None,
    )
    if movie:
        return movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie {slug!r} not found",
    )
