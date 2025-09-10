from typing import (
    Annotated,
    Optional,
)
from annotated_types import Len
from pydantic import BaseModel


class MovieBase(BaseModel):
    slug: str
    name: str
    description: Optional[str] = None
    author: Optional[str] = None


class Movie(MovieBase):
    pass


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
