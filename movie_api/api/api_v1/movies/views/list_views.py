from typing import Annotated

from api.api_v1.movies.crud import storage
from schemas.movies import (
    Movie,
    MovieCreate,
    MovieRead,
)

from fastapi import (
    APIRouter,
    status,
)

router = APIRouter(
    prefix="/movies",
    tags=["Main views"],
)


@router.get(
    "/",
    response_model=list[MovieRead],
)
def get_movies_catalog():
    return storage.get_movies()


@router.post(
    "/",
    response_model=MovieRead,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(
    movie: MovieCreate,
):
    return storage.create_movie(movie)
