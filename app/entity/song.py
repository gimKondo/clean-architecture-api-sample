from dataclasses import dataclass
from typing import Optional


@dataclass
class Song:
    id: str
    name: str
    artist_name: Optional[str]
    album_name: Optional[str]
    provider_service_name: Optional[str]
    link_url: Optional[str]
    image_url: Optional[str]
