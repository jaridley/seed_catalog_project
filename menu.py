import database
from enter_seed_information import enter_seed_information


MENU_PROMPT = '''----Seed Catalog----
Please choose one fo them following options:

1) Add seed information
2) Search seed information
3) Search seed information by name
4) Search seed information by type
5) Exit

Enter Option:
'''


def menu():
    connection = database.initialize_database()

    while (user_option := input(MENU_PROMPT)) != '5':
        if user_option == '1':
            enter_seed_information(connection)
        elif user_option == '2':
            seeds = database.get_seed_info(connection)
            for seed in seeds:
                print(seed)
        elif user_option == '3':
            name = input('Enter Seed Name:')
            seeds = database.get_seed_info_by_name(connection, name)
            for seed in seeds:
                print(seed)
        elif user_option == '4':
            seed_type = input('Enter Seed Type:')
            seeds = database.get_seed_info_by_type(connection, seed_type)
            for seed in seeds:
                print(seed)
        else:
            print('Invalid Option, try again!!!')


if __name__ == '__main__':
    menu()
