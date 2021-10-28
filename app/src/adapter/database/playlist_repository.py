import dataclasses

from ...entity.playlist import Playlist
from ...usecase.playlist_repository import PlaylistRepository
from .database_client import DatabaseClient


class PlaylistRepositoryImpl(PlaylistRepository):
    def __init__(self, client: DatabaseClient):
        self.client = client

    def register(self, playlist: Playlist) -> str:
        id = self.client.add("playlists", dataclasses.asdict(playlist))
        return id
