from dataclasses import dataclass, field
from models import Book


@dataclass
class Member:
    """ Représente un membre de la bibliothèque """
    
    full_name: str
    borrowed_books: list[Book] = field(default_factory=list)
