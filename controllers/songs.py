from fastapi import  APIRouter

songs_router=APIRouter()

@songs_router.get("/songs/{song_id}")
def get_song_by_id(song_id: str):
    return {"song_id": song_id}

@songs_router.post("/songs/save")
def save_song():
    return {"message": "Song has been saved successfully."}

@songs_router.put("/songs/{song_id}")
def update_song(song_id: str):
    return {"song_id": song_id}

@songs_router.delete("/songs/{song_id}")
def delete_song(song_id: str):
    return {"song_id": song_id}