from dataclasses import dataclass, field


@dataclass
class Book:
    """ Représente un livre dans la bibliothèque """
    
    book_title: str
    author: str
    available: bool = True

    def __str__(self):
        status = 'Disponible' if self.available else 'En prêt'
        return f'Titre : {self.book_title} \n   Auteur : {self.author} \n   Statut : {status}'
