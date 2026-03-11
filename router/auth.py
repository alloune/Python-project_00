from fastapi import APIRouter
from schemas.user import User

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
async def register(user: User):
    return user