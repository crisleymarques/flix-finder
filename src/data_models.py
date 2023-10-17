from pydantic import BaseModel, Field

class MovieDescription(BaseModel):
    genre: str | None = Field(default=None, examples=["Action"])
    decade: int | None = Field(default=None, examples=[1990])
    movie_reference: str |  None = Field(default=None, examples=["Matrix"])
