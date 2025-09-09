from typing import Annotated

from schemas.movies import Movie

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    Request,
    status,
)


MOVIES = [
    Movie(
        slug="1",
        name="Интерстеллар",
        description="Фантастический фильм о путешествии через червоточину в поисках нового дома для человечества",
        author="Кристофер Нолан",
    ),
    Movie(
        slug="2",
        name="Крестный отец",
        description="Эпическая сага о сицилийской мафиозной семье Корлеоне",
        author="Фрэнсис Форд Коппола",
    ),
    Movie(
        slug="3",
        name="Властелин колец: Братство кольца",
        description="Фэнтези о путешествии хоббита Фродо по уничтожению Кольца Всевластия",
        author="Питер Джексон",
    ),
    Movie(
        slug="4",
        name="Форрест Гамп",
        description="История жизни простого человека, ставшего свидетелем ключевых событий американской истории",
        author="Роберт Земекис",
    ),
]

app = FastAPI(
    title="Movie Catalog Api",
)


@app.get("/")
def read_root(
    request: Request,
):
    docs_url = request.url.replace(
        path="/docs",
    )
    return {
        "docs": str(docs_url),
    }


@app.get(
    "/movies/",
    response_model=list[Movie],
)
def get_movies_catalog():
    return MOVIES


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


@app.get(
    "/movies/{slug}",
    response_model=Movie,
)
def get_movie(
    movie: Annotated[
        Movie,
        Depends(found_movie),
    ],
):
    return movie
