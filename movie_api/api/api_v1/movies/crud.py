import logging

from schemas.movies import (
    Movie,
    MovieCreate,
    MoviePartialUpdate,
    MovieUpdate,
)
from core.config import MOVIE_STORAGE_FILEPATH

from pydantic import (
    BaseModel,
    ValidationError,
)

log = logging.getLogger(__name__)


class MovieStorage(BaseModel):
    slug_to_movie: dict[str, Movie] = {}

    def init_storage_from_state(self) -> None:
        try:
            data = MovieStorage.from_state()
        except ValidationError:
            self.save_state()
            log.warning("Rewritten storage file due to validation error.")

        self.slug_to_movie.update(
            data.slug_to_movie,
        )
        log.warning("Recovered data from storage file.")

    def save_state(self) -> None:
        MOVIE_STORAGE_FILEPATH.write_text(self.model_dump_json(indent=2))
        log.info("Saved movie to storage file.")

    @classmethod
    def from_state(cls) -> "MovieStorage":
        if not MOVIE_STORAGE_FILEPATH.exists():
            log.info("Movies storage file doesn't exist.")
            return MovieStorage()
        return cls.model_validate_json(MOVIE_STORAGE_FILEPATH.read_text())

    def get_movies(self) -> list[Movie]:
        return list(self.slug_to_movie.values())

    def get_movie_by_slug(self, slug: str) -> Movie | None:
        return self.slug_to_movie.get(slug)

    def create_movie(self, movie_in: MovieCreate) -> Movie:
        movie = Movie(
            **movie_in.model_dump(),
        )
        self.slug_to_movie[movie.slug] = movie
        self.save_state()
        log.info("Added new movie: %s", movie.slug)
        return movie

    def delete_by_slug(self, slug: str) -> None:
        self.slug_to_movie.pop(slug, None)
        self.save_state()

    def delete_movie(self, movie: Movie) -> None:
        self.delete_by_slug(slug=movie.slug)

    def update_movie(
        self,
        movie: Movie,
        movie_in: MovieUpdate,
    ):
        for field_name, value in movie_in:
            setattr(movie, field_name, value)
        self.save_state()
        return movie

    def update_partial_movie(
        self,
        movie: Movie,
        movie_in: MoviePartialUpdate,
    ):
        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field_name, value)
        self.save_state()
        return movie


storage = MovieStorage()
