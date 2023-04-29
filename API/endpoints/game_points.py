from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from starlette.websockets import WebSocket

from game.BoardMaker import BoardMaker
from security.UserManager import get_current_user_websocket

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "FastAPI is running"}


@router.get("/card/{card_number}")
async def card_test(card_number: int):
    return FileResponse(f"./assets/cards/{card_number}.png")


@router.get("/refresh_board")
async def refresh_board():
    board = await BoardMaker.game_start()
    return board.json()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, bah=Depends(get_current_user_websocket)):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"bah")
