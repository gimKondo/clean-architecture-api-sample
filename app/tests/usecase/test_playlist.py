from src.usecase.playlist_interactor import PlaylistInteractor

from .mock import PlaylistRepositoryMock, SongExplorerMock


def test_generate_smartly():
    interactor = PlaylistInteractor(repository=PlaylistRepositoryMock(), song_explorer=SongExplorerMock())
    playlist = interactor.generate_smartly("My Favorite", "test")
    assert playlist.id is not None
    assert playlist.name == "My Favorite"
    assert len(playlist.songs) != 0
