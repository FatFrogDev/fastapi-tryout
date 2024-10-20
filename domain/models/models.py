# db/models/album.py
from sqlalchemy import UUID, Column, Date, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

import uuid
from database import Base
from pydantic import BaseModel


class UserEntity(Base):
    __tablename__ = "users"

    user_id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    # Relationship with songs
    songs = relationship("SongEntity", back_populates="users")
    albums = relationship("AlbumEntity", back_populates="users")


# db/models/user.py

class SongEntity(Base):
    __tablename__ = "songs"

    song_id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, index=True)
    format = Column(String)
    file = Column(String)
    duration = Column(Integer)
    release_date = Column(Date, server_default=('Now()'))
    # Relationship with users
    user_id = Column(UUID, ForeignKey("users.user_id"))
    users = relationship("UserEntity", back_populates="songs")

class AlbumEntity(Base):
    __tablename__ = "albums"

    album_id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, index=True)
    release = Column(Date, server_default=('Now()'))
    # Relationship with users
    user_id = Column(UUID, ForeignKey("users.user_id"))
    users = relationship("UserEntity", back_populates="albums")


# Many to Many relationship between albums and songs

albums_songs = Table(
    'albums_songs',
    Base.metadata,
    Column('song_id', UUID, ForeignKey('songs.song_id')),
    Column('album_id', UUID, ForeignKey('albums.album_id'))
)


## Models for the DTOs

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    password: str | None = None

class UserResponse(BaseModel):
    name: str
    email: str