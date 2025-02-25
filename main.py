from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()


class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'


BANDS = [
    {'id': 1, 'name': 'The Kinks', 'genre': 'Rock'},
    {'id': 2, 'name': 'Aphex Twin', 'genre': 'Electronic'},
    {'id': 3, 'name': 'Aphex Twin', 'genre': 'Hip-hop'},
    {'id': 4, 'name': 'Aphex Twin', 'genre': 'Metal'},
]


@app.get('/')
async def read_root() ->  dict[str, str]:
    return {'message': 'Hello World'}


@app.get('/bands')
async def bands() -> list[dict]:
    return BANDS

@app.get('/bands/{id}')
async def bands(id: int) -> dict:
    for band in BANDS:
        if band['id'] == id:
            return band
    raise HTTPException(status_code=404, detail='detail not found') 



@app.get('bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]
