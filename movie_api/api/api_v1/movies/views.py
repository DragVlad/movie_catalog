from typing import Annotated

from .crud import MOVIES
from .dependencies import found_movie
from schemas.movies import (
    Movie,
    MovieCreate,
)

from fastapi import (
    APIRouter,
    Depends,
    status,
)


router = APIRouter(
    prefix="/movies",
    tags=["Awesome Movies API"],
)


@router.get(
    "/",
    response_model=list[Movie],
)
def get_movies_catalog():
    return MOVIES


@router.get(
    "/{slug}",
    response_model=Movie,
)
def get_movie(
    movie: Annotated[
        Movie,
        Depends(found_movie),
    ],
):
    return movie


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(
    movie_create: MovieCreate,
):
    return Movie(
        **movie_create.model_dump(),
    )
