from typing import Annotated

from api.api_v1.movies.crud import storage
from api.api_v1.movies.dependencies import found_movie
from schemas.movies import (
    Movie,
    MoviePartialUpdate,
    MovieUpdate,
    MovieRead,
)

from fastapi import (
    APIRouter,
    Depends,
    status,
)


router = APIRouter(
    prefix="/{slug}",
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


MovieBySlug = Annotated[
    Movie,
    Depends(found_movie),
]


@router.get(
    "/",
    response_model=MovieRead,
)
def get_movie(
    movie: MovieBySlug,
):
    return movie


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(
    movie: MovieBySlug,
) -> None:
    storage.delete_movie(movie=movie)


@router.put(
    "/",
    response_model=MovieRead,
)
def update_movie_details(
    movie: MovieBySlug,
    movie_in: MovieUpdate,
):
    return storage.update_movie(
        movie=movie,
        movie_in=movie_in,
    )


@router.patch(
    "/",
    response_model=MovieRead,
)
def update_movie_details_partial(
    movie: MovieBySlug,
    movie_in: MoviePartialUpdate,
) -> Movie:
    return storage.update_partial_movie(
        movie=movie,
        movie_in=movie_in,
    )
