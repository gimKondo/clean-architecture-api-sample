from dataclasses import dataclass
from typing import List, Optional

from .song import Song


@dataclass
class Playlist:
    id: str
    name: str
    songs: List[Song]
