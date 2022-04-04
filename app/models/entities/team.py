from sqlalchemy import Column, String
from app.models.entities.base import BaseModel


class Team(BaseModel):
    name = Column(String, nullable=False)
    description = Column(String)
