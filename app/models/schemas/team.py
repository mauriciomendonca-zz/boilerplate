from pydantic.main import BaseModel
from typing import Optional
from app.models.schemas.base import Base


class ListOfTeamsInResponse(Base):
    id: int
    name: str
    description: str


class TeamInCreate(Base):
    name: str
    description: str


class TeamInFilter(BaseModel):
    name: Optional[str]
    description: Optional[str]
