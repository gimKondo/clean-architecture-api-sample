import dataclasses
from typing import Any, Dict

from pydantic import BaseModel

from ...usecase.playlist_interactor import PlaylistInteractor


class PlaylistGenerateParam(BaseModel):
    name: str
    keyword: str

    class Config:
        schema_extra = {
            "example": {
                "name": "My Favorite 1",
                "keyword": "pillows",
            }
        }


class PlaylistController:
    def __init__(self, interactor: PlaylistInteractor):
        self.interactor = interactor

    def generate(self, param: PlaylistGenerateParam) -> Dict[str, Any]:
        playlist = self.interactor.generate_smartly(param.name, param.keyword)
        return dataclasses.asdict(playlist)
