from app.models.schemas.base import Base


class AccessTokenInCreate(Base):
    username: str
    role: str


class AccessTokenResponse(Base):
    username: str
    role: str
    access_token: str
