from sqlalchemy import Column, String
from app.models.entities.base import BaseModel


class ToTestModel(BaseModel):
    name = Column(String, nullable=False)
    description = Column(String)


def test_base_model_update():
    model = ToTestModel(name="test", description="test")
    model.update(name="test2", description="test2")
    assert model.name == "test2"
    assert model.description == "test2"


def test_base_model_clone():
    model = ToTestModel(name="test", description="test")
    clone = model.clone()
    assert clone.name == "test"
    assert clone.description == "test"
