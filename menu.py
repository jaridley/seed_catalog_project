import enter_seed_information

MENU_PROMPT = '''Seed Catalog
Please choose one fo them following options:

1) Add seed information
2) Search seed information
3) Exit

Enter Option:
'''

def menu():
    while (user_option := input(MENU_PROMPT)) != '3':
        if user_option == 1:

        elif user_option == 2:
            pass
        else:
            print('Invalid Option, try again!!!')

if __name__ == '__main__':
    menu()