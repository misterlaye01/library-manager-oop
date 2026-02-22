from dataclasses import dataclass, field
from models import Book


@dataclass
class Member:
    full_name: str
    borrowed_book: list[Book] = field(default_factory=list)
