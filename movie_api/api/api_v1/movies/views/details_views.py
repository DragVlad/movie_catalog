from typing import Annotated

from api.api_v1.movies.crud import storage
from api.api_v1.movies.dependencies import found_movie
from schemas.movies import (
    Movie,
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


@router.get(
    "/",
    response_model=Movie,
)
def get_movie(
    movie: Annotated[
        Movie,
        Depends(found_movie),
    ],
):
    return movie


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(
    movie: Annotated[
        Movie,
        Depends(found_movie),
    ],
) -> None:
    storage.delete_movie(movie=movie)
