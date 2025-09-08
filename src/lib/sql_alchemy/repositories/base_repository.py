from dataclasses import dataclass
from typing import Generic, Type, TypeVar
from src.lib.sql_alchemy.engine import db

T = TypeVar("T")


@dataclass
class BaseRepository(Generic[T]):
    entity: Type[T]

    def create(self, new_item: T) -> T:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item

    def get_by_id(self, id: int) -> T:
        item = db.get_one(self.entity, id)
        return item

    def get_all(self, limit: int | None = 10) -> list[T]:
        all_items = db.query(self.entity).limit(limit).all()
        return all_items

    def update(self, id: int, new_item: T):
        item = self.get_by_id(id)
        for key in item.__dict__.keys():
            new_value = new_item.__getattribute__(key)
            item.__setattr__(key, new_value)

        db.commit()
        return item

    def delete(self, id: int):
        item = self.get_by_id(id)
        db.delete(item)
        db.commit()
