from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.endpoints import map
import uvicorn


app = FastAPI(debug=False)

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origin_regex=r'https?:\/\/.*\.?ortieom\.ru'
)

app.include_router(map.router)

if __name__ == '__main__':
    # uvicorn.run(app, host='veloapi.ortieom.ru', port=8000)
    uvicorn.run(app, host='0.0.0.1', port=8000)
