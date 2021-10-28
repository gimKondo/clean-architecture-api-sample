import dataclasses
from typing import List

from src.entity.playlist import Playlist
from src.entity.song import Song
from src.usecase.playlist_repository import PlaylistRepository
from src.usecase.song_explorer import SongExplorer


class PlaylistRepositoryMock(PlaylistRepository):
    def __init__(self):
        self.playlists = []

    def register(self, playlist: Playlist) -> str:
        id = 1
        copied = dataclasses.replace(playlist, id=id)
        self.playlists.append(copied)
        return id


class SongExplorerMock(SongExplorer):
    def explore(self, keyword: str) -> List[Song]:
        return [
            Song(
                name="街",
                artist_name="SOPHIA",
                album_name=None,
                provider_service_name="mock",
                link_url=None,
                image_url=None,
            ),
            Song(
                name="Young Boy",
                artist_name="Paul McCartney",
                album_name=None,
                provider_service_name="mock",
                link_url=None,
                image_url=None,
            ),
            Song(
                name="MY FOOT",
                artist_name="the pillows",
                album_name=None,
                provider_service_name="mock",
                link_url=None,
                image_url=None,
            ),
        ]
