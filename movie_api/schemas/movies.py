from typing import (
    Annotated,
    Optional,
)
from annotated_types import (
    Len,
    MaxLen,
)
from pydantic import BaseModel


class MovieBase(BaseModel):
    description: Optional[str] = None
    author: Optional[str] = None


class Movie(MovieBase):
    slug: str
    name: str
    viewers: int


class MovieCreate(Movie):
    slug: Annotated[
        str,
        Len(
            min_length=3,
            max_length=10,
        ),
    ]
    name: Annotated[
        str,
        Len(
            min_length=5,
            max_length=20,
        ),
    ]


class MovieUpdate(MovieBase):
    description: Annotated[
        str,
        MaxLen,
    ]


class MoviePartialUpdate(MovieBase):
    description: str | None = None
    author: str | None = None


class MovieRead(MovieBase):
    slug: str
    name: str
