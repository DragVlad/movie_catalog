from api.api_v1.movies.crud import storage
from api.api_v1.movies.dependencies import save_storage_state
from schemas.movies import (
    MovieCreate,
    MovieRead,
)

from fastapi import APIRouter, status, Depends

router = APIRouter(
    prefix="/movies",
    tags=["Main views"],
    dependencies=[Depends(save_storage_state)],
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
