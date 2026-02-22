from services import LibraryManager


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


def run():
    library = LibraryManager()

    library.add_book('Une si longue lettre', 'Mariama BA')
    library.add_book('Vol de nuit', 'Antoine de Saint-Exupéry')
    library.add_book("Sous l'orage", 'Seydou Bodjan')

    library.register_members('Abdoulaye DIALLO')
    library.register_members('Cheikh Saliou TALLA')


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