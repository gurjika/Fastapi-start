from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, BandWithId, BandCreate, BandBase
from typing import Union

app = FastAPI()



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
async def bands(
    genre: GenreURLChoices=None, 
    has_albums: bool = False) -> list[BandWithId]:
    band_list = [BandWithId(**b) for b in BANDS]
    if genre:
        band_list = [
            b for b in band_list if b['genre'].lower() == genre.value
        ]
    
    if has_albums:
        band_list = [b for b in band_list if len(b.albums) > 0]

    return band_list


@app.get('/bands/{id}')
async def bands(id: int) -> BandWithId:
    for band in BANDS:
        if band['id'] == id:
            return BandWithId(**band)
    raise HTTPException(status_code=404, detail='detail not found') 



@app.get('bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]

