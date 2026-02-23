import functools
from datetime import datetime
from models import Book, Member


def log_action(function):
    """ Enregistre chaque action de prêt dans un fichier log.txt """

    @functools.wraps(function)
    def wrapper(self, member_name: str, book_title: str):
        try:
            function(self, member_name, book_title)
            with open('log.txt', 'a', encoding='utf-8') as file:
                file.write(f'[{datetime.now().strftime('%d/%m/%Y - %H:%M:%S')}] - Prêt validé : {book_title} prêté à {member_name}\n')
        except Exception as e:
            with open('log.txt', 'a', encoding='utf-8') as file:
                file.write(f'[{datetime.now().strftime('%d/%m/%Y - %H:%M:%S')}] - Tentative de prêt échouée : {member_name} voulait emprunter {book_title} - [{e}]\n')
    return wrapper


class LibraryManager:
    """ Gestionnaire de la bibliothèque """
    
    def __init__(self):
        self.members_list = []
        self.book_list = []
    
    def find_book(self, title: str):
        for book in self.book_list:
            if book.book_title.lower() == title.strip().lower():
                return book
        return None
    
    def find_member(self, full_name: str):
        for member in self.members_list:
            if member.full_name.lower() == full_name.strip().lower():
                return member
        return None

    def add_book(self, book_title: str, author: str):
        if self.find_book(book_title) is not None:
            raise ValueError(f'{book_title} existe déjà dans la bibliothèque.')
        
        book = Book(book_title, author)
        self.book_list.append(book)
        print(f'{book_title} ajouté dans la biblothèque.')
    
    def register_member(self, full_name: str):
        if self.find_member(full_name) is not None:
            raise ValueError(f'{full_name} est déjà inscrit.')
        
        member = Member(full_name)
        self.members_list.append(member)
        print(f'{full_name} inscrit dans le registre de la biblothèque.')
    
    @log_action
    def validate_loan(self, member_name: str, book_title: str):
        member = self.find_member(member_name)
        if member is None:
            raise ValueError(f'Membre introuvable !')
        
        book = self.find_book(book_title)
        if book is None:
            raise ValueError(f'Livre introuvable !')
        
        if not book.available:
            raise PermissionError(f'Le livre est déjà emprunté.')
        
        book.available = False
        member.borrowed_books.append(book)
        print(f'Prêt validé : {book.book_title} prêté à {member.full_name}')
    
    def return_book(self, member_name: str, book_title: str):
        member = self.find_member(member_name)
        if member is None:
            raise ValueError(f'Membre introuvable !')
        
        book = self.find_book(book_title)
        if book is None:
            raise ValueError(f'Livre introuvable !')
        
        if book not in member.borrowed_books:
            raise PermissionError(f"{member_name} n'a pas emprunté {book_title}.")
        
        book.available = True
        member.borrowed_books.remove(book)
        print(f'Retour enregistré : {book.book_title} rendu par {member.full_name}.')
    
    def display_books(self):
        print('\n------- CATALOGUE -------')
        if not self.book_list:
            print('Aucun livre enregistré')
            return
        
        for i, book in enumerate(self.book_list, 1):
            print(f'{i}. {book}')
    
    def display_members(self):
        print('\n------- MEMBRES -------')
        if not self.members_list:
            print('Aucun membre enregistré')
            return
        
        for i, member in enumerate(self.members_list, 1):
            print(f'{i}. {member}')
