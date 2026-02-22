from models import Book, Member


class LibraryManager:
    def __init__(self):
        self.members_list = []
        self.book_list = []
    
    def find_book(self, title):
        for book in self.book_list:
            if book.book_title.lower() == title.strip().lower():
                return book
        return None
    
    def find_member(self, full_name):
        for member in self.members_list:
            if member.full_name.lower() == full_name.strip().lower():
                return member
        return None

    def add_book(self, book_title, author):
        if self.find_book(book_title) is not None:
            raise ValueError(f'{book_title} existe déjà dans la bibliothèque.')
        
        book = Book(book_title, author)
        self.book_list.append(book)
        print(f'{book_title} ajouté dans la biblothèque.')
    
    def register_members(self, full_name):
        if self.find_member(full_name) is not None:
            raise ValueError(f'{full_name} est déjà inscrit.')
        
        member = Member(full_name)
        self.members_list.append(member)
        print(f'{full_name} inscrit dans le registre de la biblothèque.')
    
    def validate_loan(self, member_name, book_title):
        member = self.find_member(member_name)
        if member is None:
            raise ValueError(f'Membre introuvable !')
        
        book = self.find_book(book_title)
        if book is None:
            raise ValueError(f'Livre introuvable !')
        
        if not book.available:
            raise PermissionError(f'Le livre est déjà emprunté.')
        
        book.available = False
        member.borrowed_book.append(book)
        print(f'Prêt validé : {book.book_title} prêté à {member.full_name}')
    
    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if member is None:
            raise ValueError(f'Membre introuvable !')
        
        book = self.find_book(book_title)
        if book is None:
            raise ValueError(f'Livre introuvable !')
        
        if book not in member.borrowed_book:
            raise PermissionError(f"{member_name} n'a pas emprunté {book_title}.")
        
        book.available = True
        member.borrowed_book.remove(book)
        print(f'Retour enregistré : {book.book_title} rendu par {member.full_name}.')
    
    def display_books(self):
        print('\n------- CATALOGUE -------')
        if not self.book_list:
            print('Aucun livre enregistré')
        
        for i, book in enumerate(self.book_list, 1):
            print(f'{i}. {book}')
    
    def display_members(self):
        print('\n------- CATALOGUE -------')
        if not self.members_list:
            print('Aucun membre enregistré')
        
        for i, member in enumerate(self.members_list, 1):
            print(f'{i}. {member}')
