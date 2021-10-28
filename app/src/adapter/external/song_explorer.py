from typing import Dict, List

from ...entity.song import Song
from ...usecase.song_explorer import SongExplorer
from .api_client import ApiClient


class SongExplorerByAPI(SongExplorer):
    def __init__(self, client: ApiClient):
        self.client = client

    def explore(self, keyword: str) -> List[Song]:
        query = f"?term={keyword}&country=jp&media=music&entity=song&limit=10"
        songs = self.client.search(query)
        return [self._parse_search_result(e) for e in songs.get("results")]

    def _parse_search_result(self, result: Dict) -> Song:
        return Song(
            name=result.get("trackName"),
            artist_name=result.get("artistName"),
            album_name=result.get("collectionName"),
            provider_service_name="iTunes",
            link_url=result.get("trackViewUrl"),
            image_url=result.get("artworkUrl60"),
        )
