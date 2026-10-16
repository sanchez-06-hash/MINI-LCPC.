
import os
import jwt
from datetime import datetime, timedelta, timezone


SECRET_KEY = os.environ.get("MINI_LCPC_SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError(
        "Set the MINI_LCPC_SECRET_KEY environment variable before starting the app."
    )

ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 60


def create_access_token(username: str, role: str) -> str:
    now = datetime.now(timezone.utc)

    payload = {
        "sub": username,
        "role": role,
        "iat": now,
        "exp": now + timedelta(minutes=TOKEN_EXPIRE_MINUTES),
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):
    try:
        return jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
    except jwt.InvalidTokenError:
        return None