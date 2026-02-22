class Book:
    def __init__(self, book_title, author):
        self.book_title = book_title
        self.author = author
        self.available = True
    
    def __str__(self):
        status = 'Disponible' if self.available else 'En prêt'
        return f'Titre : {self.book_title} \n   Auteur : {self.author} \n   Statut : {status}'


class Member:
    def __init__(self, full_name):
        self.full_name = full_name
        self.borrowed_book = []
    
    def __str__(self):
        if not self.borrowed_book:
            return f'{self.full_name} - Aucun emprunt en cours'
        
        # for book in self.borrowed_book:
        #     book.book_title
        
        # return f'{self.full_name} - Emprunts : {book.book_title}'


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





library = LibraryManager()

library.add_book('Une si longue lettre', 'Mariama BA')
library.add_book('Vol de nuit', 'Antoine de Saint-Exupéry')
library.add_book("Sous l'orage", 'Seydou Bodjan')

library.register_members('Abdoulaye DIALLO')
library.register_members('Cheikh Saliou TALLA')


def user_input(text):
    user_input = input(text).strip()
    if not user_input:
        raise ValueError('Ce champ ne peut pas être vide.')
    return user_input

def display_menu():
    print(
        """\n------ GESTIONNAIRE DE BIBLIOTHÈQUE ------
        1. Ajouter un livre
        2. Inscrire un membre
        3. Valider un prêt
        4. Enregistrer un retour
        5. Afficher tous les livres
        6. Afficher tous les membres
        0. Quitter
        """
    )


while True:
    display_menu()

    choice = input('Choisissez une option valide : ').strip()

    if not choice.isdigit():
        print('Veuillez choisir une option valide.')
        continue

    try:
        match choice:
            case '1':
                print('\n------- AJOUTER UN LIVRE -------')
                title = user_input('Titre : ')
                author = user_input('Auteur : ')
                library.add_book(title, author)
            
            case '2':
                print('\n------- INSCRIRE UN MEMBRE -------')
                full_name = user_input('Nom complet : ')
                library.register_members(full_name)
            
            case '3':
                print('\n------- VALIDER UN PRÊT -------')
                member_name = user_input('Nom complet : ')
                book_title = user_input('Titre du livre : ')
                library.validate_loan(member_name, book_title)
            
            case '4':
                print('\n------- ENREGISTRER UN RETOUR -------')
                member_name = user_input('Nom complet : ')
                book_title = user_input('Titre du livre : ')
                library.return_book(member_name, book_title)
            
            case '5':
                library.display_books()
            
            case '6':
                library.display_members()
            
            case '0':
                print('\nJajeuf !')
                break

            case _:
                print('Entrez une option valide')
    except (ValueError, PermissionError) as e:
        print(f'\nERREUR : {e}')