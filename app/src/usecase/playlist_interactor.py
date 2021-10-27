from ..entity.playlist import Playlist
from .playlist_repository import PlaylistRepository


class PlaylistInteractor:
    def __init__(self, repository: PlaylistRepository):
        self.repository = repository

    def generate_smartly(self, keyword: str) -> Playlist:
        """キーワードからいい感じにプレイリストを作る

        Args:
            keyword (str): プレイリストを生成するためのキーワード

        Returns:
            Playlist: プレイリスト
        """

        playlist = Playlist(id="dummy", name="Favorite1", songs=[])
        self.repository.register(playlist)
        return playlist
