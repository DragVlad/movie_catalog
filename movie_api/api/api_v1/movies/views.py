from typing import Annotated

from .crud import storage
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
    return storage.get_movies()


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
    movie: MovieCreate,
):
    return storage.create_movie(movie)


@router.delete(
    "/{slug}/",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_204_NO_CONTENT: {
            "description": "Succeful delete",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Movie slug:'slug' delete",
                    },
                },
            },
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Short URL not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Movie slug:'slug' not found",
                    },
                },
            },
        },
    },
)
def delete_movie(
    movie: Annotated[
        Movie,
        Depends(found_movie),
    ],
) -> None:
    storage.delete_movie(movie=movie)
