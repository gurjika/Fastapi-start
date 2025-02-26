from enum import Enum
from pydantic import BaseModel, field_validator
from datetime import date

class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'


class GenreChoices(Enum):
    ROCK = 'Rock'
    ELECTRONIC = 'Electronic'
    METAL = 'Metal'
    HIP_HOP = 'Hip-Hop' 
   
class Album(BaseModel):
    title:str
    release_date: date

class BandBase(BaseModel):
    name: str
    genre: GenreChoices
    albums: list[Album] = []

    @field_validator('genre', mode='before')
    def title_case_genre(cls, value):
        if isinstance(value, str):
            return GenreChoices(value.title())
        return value

class BandCreate(BandBase):
    pass

class BandWithId(BandBase):
    id: int



