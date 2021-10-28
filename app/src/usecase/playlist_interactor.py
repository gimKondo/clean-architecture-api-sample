from ..entity.playlist import Playlist
from .playlist_repository import PlaylistRepository
from .song_explorer import SongExplorer


class PlaylistInteractor:
    def __init__(self, repository: PlaylistRepository, song_explorer: SongExplorer):
        self.repository = repository
        self.song_explorer = song_explorer

    def generate_smartly(self, name: str, keyword: str) -> Playlist:
        """キーワードからいい感じにプレイリストを作る

        - プレイリストの作成

        Args:
            name (str): プレイリスト名
            keyword (str): プレイリストを生成するためのキーワード

        Returns:
            Playlist: プレイリスト
        """

        songs = self.song_explorer.explore(keyword)
        playlist = Playlist(id="dummy", name=name, songs=songs)
        self.repository.register(playlist)
        return playlist
