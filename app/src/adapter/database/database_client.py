from abc import ABC, abstractmethod
from typing import Dict, Union


class DatabaseClient(ABC):
    @abstractmethod
    def add(self, collection_name: str, document: Dict[str, Union[str, int, float]]):
        pass
