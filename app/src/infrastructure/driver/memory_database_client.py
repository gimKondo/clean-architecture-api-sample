from typing import Dict, List, Union

from ...adapter.database.database_client import DatabaseClient


class MemoryDatabaseClient(DatabaseClient):
    def __init__(self):
        # key: コレクション名
        # value: コレクション値 = 配列インデクスをIDとしたドキュメントリスト
        self.collections: Dict[str, List] = {}

    def add(self, collection_name: str, document: Dict[str, Union[str, int, float]]):
        if collection_name not in self.collections:
            self.collections["collection_name"] = []
        id = len(self.collections[collection_name])
        self.collections[collection_name].append(document)
        return f"{id}"
