import database
from enter_seed_information import enter_seed_information


MENU_PROMPT = '''----Seed Catalog----
Please choose one fo them following options:

1) Add seed information
2) Search seed information
3) Update seed information
4) Exit

Enter Option:
'''


def menu():
    connection = database.initialize_database()

    while (user_option := input(MENU_PROMPT)) != '4':
        if user_option == '1':
            enter_seed_information(connection)
        elif user_option == '2':
            pass
        elif user_option == '3':
            pass
        else:
            print('Invalid Option, try again!!!')


if __name__ == '__main__':
    menu()
