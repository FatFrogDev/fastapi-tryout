from fastapi import  APIRouter

albums_router = APIRouter()



@albums_router.get("/albums/{album_id}")
def get_album_by_id(album_id: str):
    return {"album_id": album_id}

@albums_router.post("/albums/save")
def save_album():
    return {"message": "Album has been saved successfully."}

@albums_router.put("/albums/{album_id}")
def update_album(album_id: str):
    return {"album_id": album_id}

@albums_router.delete("/albums/{album_id}")
def delete_album(album_id: str):
    return {"album_id":album_id}