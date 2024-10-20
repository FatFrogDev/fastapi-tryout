from typing import Union

from fastapi import FastAPI, APIRouter

from controllers.users import users_router as users
from controllers.songs import songs_router as songs 
from controllers.albums import albums_router as albums

from database import engine
from database import Base   

# API Setup

app = FastAPI()
router = APIRouter()

Base.metadata.create_all(bind=engine)

# Router register
app.include_router(users)
app.include_router(songs)
app.include_router(albums)


@app.get("/")
def read_root():
    return ["Hello World"]
