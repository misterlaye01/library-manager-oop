from dataclasses import dataclass, field


@dataclass
class Book:
    book_title: str
    author: str
    available: bool = field(default=True)

    def __str__(self):
        status = 'Disponible' if self.available else 'En prêt'
        return f'Titre : {self.book_title} \n   Auteur : {self.author} \n   Statut : {status}'
