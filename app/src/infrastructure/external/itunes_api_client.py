import json
from typing import Any, Dict

import requests

from ...adapter.external.api_client import ApiClient

ITUNES_SEARCH_API_URL = "https://itunes.apple.com/search"


class ITunesApiClient(ApiClient):
    def search(self, params: Dict[str, str]) -> Dict[str, Any]:
        res = requests.get(ITUNES_SEARCH_API_URL, params=params)
        return json.loads(res.text)
