import database


MENU_PROMPT = '''Seed Catalog
Please choose one fo them following options:

1) Add seed information
2) Search seed information
3) Exit

Enter Option:
'''

def menu():
    connection = database.initialize_database()

    while (user_option := input(MENU_PROMPT)) != '3':
        if user_option == '1':
            seed_name = input('Enter Seed Name:')
            seed_variety = input('Variety:')
            seed_type = input('Enter Seed Type:')
            seed_planting_zone = input('Enter Planting Zone:')
            germination_period = input('Enter Seed Gem Period(#days):')
            days_to_harvest = input('Days to Harvest:')
            plant_spacing = input('Enter Plant Spacing(in):')
            row_spacing = input('Enter Row Spacing(in):')
            depth = input('Enter Plant Depth(in):')
            sun_requirements = input('How much sun required?:')
            water_requirements = input('How often to water?:')

            seed_information = {
                'name': f'{seed_name}',
                'variety': f'{seed_variety}',
                'type': f'{seed_type}',
                'zone': f'{seed_planting_zone}',
                'germ_period': f'{germination_period}',
                'harvest': f'{days_to_harvest}',
                'plant_spacing': f'{plant_spacing}',
                'row_spacing': f'{row_spacing}',
                'depth': f'{depth}',
                'sun_req': f'{sun_requirements}',
                'water_req': f'{water_requirements}'
            }
            database.add_seed_info(connection, seed_information)
        elif user_option == '2':
            pass
        else:
            print('Invalid Option, try again!!!')

if __name__ == '__main__':
    menu()