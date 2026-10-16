
from fastapi import APIRouter, HTTPException
from schemas import LoginRequest
from database import get_user_by_username
from auth import verify_password
from security import create_access_token

router = APIRouter()


@router.post("/login")
def login(data: LoginRequest):
    user = get_user_by_username(data.username)

    if user is None or not verify_password(
        data.password,
        user["password_hash"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token(
        user["username"],
        user["role"]
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user["role"]
    }