from typing import Any, Dict

from fastapi import FastAPI, HTTPException

from .adapter.controller.playlist_controller import (
    PlaylistController,
    PlaylistGenerateParam,
)
from .adapter.database.playlist_repository import PlaylistRepositoryImpl
from .adapter.external.song_explorer import SongExplorerByAPI
from .infrastructure.driver.memory_database_client import MemoryDatabaseClient
from .infrastructure.external.itunes_api_client import ITunesApiClient
from .infrastructure.framework.playlist_schema import PlaylistGenerateResponse
from .usecase.playlist_interactor import PlaylistInteractor

app = FastAPI(
    title="Playlist Maker",
    version="0.1.0",
)

playlist_controller = PlaylistController(
    PlaylistInteractor(
        PlaylistRepositoryImpl(
            MemoryDatabaseClient()
        ),
        SongExplorerByAPI(
            ITunesApiClient()
        )
    ),

)

@app.post("/playlist/generate", response_model=PlaylistGenerateResponse)
async def generate_playlist(request: PlaylistGenerateParam) -> Dict[str, Any]:
    response = playlist_controller.generate(request)
    print(response)
    return response
