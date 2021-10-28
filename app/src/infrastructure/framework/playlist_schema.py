from typing import List, Optional

from pydantic import BaseModel


class SongSchema(BaseModel):
    name: str
    artist_name: Optional[str]
    album_name: Optional[str]
    provider_service_name: Optional[str]
    link_url: Optional[str]
    image_url: Optional[str]


class PlaylistGenerateResponse(BaseModel):
    id: str
    name: str
    songs: List[SongSchema]

    class Config:
        schema_extra = {
            "example": {
                "name": "My Favorite 1",
                "songs": [
                    {
                        "name": "曲1",
                        "artist_name": "アーティスト1",
                        "album_name": "アルバム1",
                        "provider_service_name": "iTunes",
                        "link_url": "https://example.com/1",
                        "image_url": "https://example.com/1.jpg",
                    },
                    {
                        "name": "曲2",
                        "artist_name": "アーティスト1",
                        "album_name": "アルバム1",
                        "provider_service_name": "iTunes",
                        "link_url": "https://example.com/2",
                        "image_url": "https://example.com/2.jpg",
                    },
                ],
            }
        }
