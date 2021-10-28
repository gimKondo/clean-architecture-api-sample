from typing import Dict, List

from ...entity.song import Song
from ...usecase.song_explorer import SongExplorer
from .api_client import ApiClient


class SongExplorerByAPI(SongExplorer):
    def __init__(self, client: ApiClient):
        self.client = client

    def explore(self, keyword: str) -> List[Song]:
        params = {
            "term": keyword,
            "country": "jp",
            "media": "music",
            "entity": "song",
            "limit": "10",
        }
        songs = self.client.search(params)
        results = songs.get("results") or []
        return [self._parse_search_result(e) for e in results]

    def _parse_search_result(self, result: Dict) -> Song:
        return Song(
            name=result.get("trackName") or "Unknown",
            artist_name=result.get("artistName"),
            album_name=result.get("collectionName"),
            provider_service_name="iTunes",
            link_url=result.get("trackViewUrl"),
            image_url=result.get("artworkUrl60"),
        )
