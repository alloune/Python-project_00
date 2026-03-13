from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer as auth_bearer
from router.auth import router as auth_router
from router.cards import router as card_router


app = FastAPI()
app.include_router(auth_router)
app.include_router(card_router)