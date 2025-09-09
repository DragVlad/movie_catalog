from pydantic import BaseModel


class MovieBase(BaseModel):
    slug: str
    name: str
    description: str
    author: str


class Movie(MovieBase):
    pass
