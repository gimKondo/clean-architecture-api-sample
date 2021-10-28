from abc import ABC, abstractmethod
from typing import List

from ..entity.song import Song


class SongExplorer(ABC):
    @abstractmethod
    def explore(self, keyword: str) -> List[Song]:
        pass
