from pydantic import BaseModel


class MovieDescription(BaseModel):
    genre: str | None = None
    decade: int | None = None
    movie_reference: str | None = None
