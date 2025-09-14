from schemas.movies import (
    Movie,
    MovieCreate,
)

from pydantic import BaseModel


class MovieStorage(BaseModel):
    slug_to_movie: dict[str, Movie] = {}

    def get_movies(self) -> list[Movie]:
        return list(self.slug_to_movie.values())

    def get_movie_by_slug(self, slug: str) -> Movie | None:
        return self.slug_to_movie.get(slug)

    def create_movie(self, movie_in: MovieCreate) -> Movie:
        movie = Movie(
            **movie_in.model_dump(),
        )
        self.slug_to_movie[movie.slug] = movie
        return movie

    def delete_by_slug(self, slug: str) -> None:
        self.slug_to_movie.pop(slug, None)

    def delete_movie(self, movie: Movie) -> None:
        self.delete_by_slug(slug=movie.slug)


storage = MovieStorage()

storage.create_movie(
    Movie(
        slug="stlr",
        name="Интерстеллар",
        description="Фантастический фильм о путешествии через червоточину в поисках нового дома для человечества",
        author="Кристофер Нолан",
    ),
)
storage.create_movie(
    Movie(
        slug="fthr",
        name="Крестный отец",
        description="Эпическая сага о сицилийской мафиозной семье Корлеоне",
        author="Фрэнсис Форд Коппола",
    ),
)
storage.create_movie(
    Movie(
        slug="lrdrng",
        name="Властелин колец: Братство кольца",
        description="Фэнтези о путешествии хоббита Фродо по уничтожению Кольца Всевластия",
        author="Питер Джексон",
    ),
)
storage.create_movie(
    Movie(
        slug="gmp",
        name="Форрест Гамп",
        description="История жизни простого человека, ставшего свидетелем ключевых событий американской истории",
        author="Роберт Земекис",
    ),
)
