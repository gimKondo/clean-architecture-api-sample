from abc import ABC, abstractmethod
from typing import Any, Dict


class ApiClient(ABC):
    @abstractmethod
    def search(self, params: Dict[str, str]) -> Dict[str, Any]:
        pass
