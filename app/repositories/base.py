from typing import Generic, TypeVar

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.database import Base

ModelT = TypeVar("ModelT", bound=Base)


class BaseRepository(Generic[ModelT]):
    def __init__(self, db: Session, model: type[ModelT] | None = None):
        self.db = db
        self.model = model or getattr(type(self), "model")

    def list(self, offset: int = 0, limit: int = 50) -> tuple[list[ModelT], int]:
        items = self.db.scalars(select(self.model).offset(offset).limit(limit)).all()
        total = self.db.scalar(select(func.count()).select_from(self.model)) or 0
        return list(items), total

    def get(self, **criteria) -> ModelT | None:
        statement = select(self.model)
        for field, value in criteria.items():
            statement = statement.where(getattr(self.model, field) == value)
        return self.db.scalar(statement)

    def add(self, entity: ModelT) -> ModelT:
        self.db.add(entity)
        return entity

    def delete(self, entity: ModelT) -> None:
        self.db.delete(entity)
