from abc import ABC, abstractmethod

from ..entity.playlist import Playlist


class PlaylistRepository(ABC):
    @abstractmethod
    def register(self, playlist: Playlist) -> str:
        pass
