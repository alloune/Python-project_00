from fastapi import FastAPI, APIRouter, Depends, HTTPException
from typing import Annotated
from schemas.login_info import LoginInfo
from schemas.user import User
from services.auth_service import get_current_user, create_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    token = await create_token(form_data.username, form_data.password)
    if not token:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
async def current_user(current_user: User = Depends(get_current_user)):
    return current_user