from time import time
from typing import Dict
import jwt
from app.config import config
from app.models.schemas.access_token import AccessTokenResponse


def sign_jwt(
    username: str, role="user", seconds_to_expire=config.JWT_SECONDS_TO_EXPIRE
) -> AccessTokenResponse:
    payload = {"username": username, "role": role}
    if seconds_to_expire > 0:
        payload["exp"] = int(time()) + seconds_to_expire

    token = jwt.encode(payload, config.JWT_SECRET, config.JWT_ALGORITHM)

    response = AccessTokenResponse(username=username, role=role, access_token=token)
    return response


def decode_jwt(token: str) -> Dict:
    try:
        decoded = jwt.decode(token, config.JWT_SECRET, [config.JWT_ALGORITHM])
        return decoded
    except:
        return None
