from dataclasses import dataclass
from dataclasses import field as fc_field
from datetime import datetime

from catalog.errors import DuplicatedIdError, ObjectIsNotFoundError


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
            if not isinstance(content, str):
                raise TypeError(f"{field} must be str")
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
    """
    Catalog of books.

    Iteration order follows the insertion order.
    """

    _items: dict[str, Book] = fc_field(default_factory=dict)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return self._items.values().__iter__()

    def __contains__(self, item_id: str) -> bool:
        return item_id in self._items

    def add(self, item: Book) -> None:
        if item.id in self._items:
            raise DuplicatedIdError

        self._items[item.id] = item

    def get(self, item_id: str) -> Book:
        if item_id in self._items:
            return self._items[item_id]

        raise ObjectIsNotFoundError

    def remove(self, item_id: str):
        if item_id in self._items:
            item = self._items.pop(item_id)
            return f"Book {item} is deleted"

        raise ObjectIsNotFoundError

    def find_by_category(self, category: str):
        books = []
        for item in self._items.values():
            if item.category == category:
                books.append(item)

        return books

    def find_by_name(self, query: str):
        books = []
        for item in self._items.values():
            if query.casefold() in item.name.casefold():
                books.append(item)

        return books
