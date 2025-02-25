from fastapi import FastAPI, HTTPException

app = FastAPI()

BANDS = [
    {'id': 1, 'name': 'The Kinks', 'genre': 'Rock'},
    {'id': 2, 'name': 'Aphex Twin', 'genre': 'Electronic'},
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




