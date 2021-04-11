import sqlite3
from sqlite3 import Error


def initialize_database():
    try:
        return sqlite3.connect('/Users/jaridley/Database/seed_catalog.db')
    except Error:
        print(f'executing {Error}')


def create_seed_table(connect):
    with connect:
        try:
            connect.execute()
        except Error:
            print(f'Getting {Error}')


def add_seed_info(connect, seed_information):
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in seed_information.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in seed_information.values())
    insert_seed = 'INSERT INTO %s ( %s ) VALUES ( %s );' % ('seed_information', columns, values)
    with connect:
        try:
            connect.execute(insert_seed)
            print(f'Information entered successfully')
        except Error:
            print(f'Info not loading {Error}')


def get_all_seed_info(connect):
    with connect:
        try:
            connect.execute()
        except Error:
            print(Error)
