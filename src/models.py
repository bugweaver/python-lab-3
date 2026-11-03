from dataclasses import dataclass
from datetime import datetime


@dataclass
class Book:
    id: str
    name: str
    category: str
    author: str
    date: datetime
    rating: int | float

    def __post_init__(self):
        fields = ("id", "name", "category", "author")

        for field in fields:
            content = getattr(self, field)
            if not content.strip():
                raise ValueError(f"{field} can not be empty!")

        if not isinstance(self.date, datetime):
            raise TypeError("The type of the date is not datetime!")

        if not isinstance(self.rating, (int, float)):
            raise TypeError("The type of the rating is not an int or a float!")

        if not (0 <= self.rating <= 5):
            raise ValueError("Rating must be from 0 to 5")


@dataclass
class Catalog:
    _items: dict[str, Book]

    def __len__(self) -> int:
        pass

    def __iter__(self):
        pass

    def __contains__(self, item_id: str):
        pass

    def add(self, item: Book):
        pass

    def get(self, item_id: str):
        pass

    def remove(self, item_id: str):
        pass

    def find_by_category(self, category: str):
        pass

    def find_by_name(self, query: str):
        pass
