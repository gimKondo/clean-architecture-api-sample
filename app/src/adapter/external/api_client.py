from abc import ABC, abstractmethod
from typing import Any, Dict


class ApiClient(ABC):
    @abstractmethod
    def search(self, query: str) -> Dict[str, Any]:
        pass
