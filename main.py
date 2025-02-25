from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, Band


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
async def bands() -> list[Band]:
    return [
        Band(**b) for b in BANDS
    ]

@app.get('/bands/{id}')
async def bands(id: int) -> Band:
    for band in BANDS:
        if band['id'] == id:
            return Band(**band)
    raise HTTPException(status_code=404, detail='detail not found') 



@app.get('bands/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [
        b for b in BANDS if b['genre'].lower() == genre.value
    ]
