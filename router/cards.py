from fastapi import APIRouter, Depends
from typing import Annotated
from main import auth_bearer
router = APIRouter(prefix="/cards", tags=["cards"])
oauth2_scheme = auth_bearer(tokenUrl="auth/login")

@router.get("/")
async def get_cards(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"message": "Voici la liste des cartes"}