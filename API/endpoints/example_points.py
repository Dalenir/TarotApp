import json

from fastapi import APIRouter
from fastapi.responses import FileResponse


from game.Board import Board

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "FastAPI is running"}


@router.get("/card/{card_number}")
async def card_test(card_number: int):
    return FileResponse(f"./assets/cards/{card_number}.gif")

@router.get("/refresh_board")
async def refresh_board():
    a = await Board.game_start()
    return a.json()
