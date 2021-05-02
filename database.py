import sqlite3
from sqlite3 import Error

LIST_INFO = 'SELECT * FROM seed_information;'
SEED_BY_NAME = 'SELECT * FROM seed_information where Name = ?'
SEED_BY_TYPE = 'SELECT * FROM seed_information where Type = ?'


def initialize_database():
    try:
        return sqlite3.connect('/Users/jaridley/Database/seed_catalog.db')
    except Error:
        print(f'Did not connect successfully because of {Error}')


def create_seed_table(connect):
    with connect:
        try:
            connect.execute()
        except Error:
            print(f'Did not create table successfully because of {Error}')


def add_seed_info(connect, seed_information):
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in seed_information.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in seed_information.values())
    insert_seed = 'INSERT INTO %s ( %s ) VALUES ( %s );' % ('seed_information', columns, values)
    with connect:
        try:
            connect.execute(insert_seed)
            print(f'Seed information entered successfully')
        except Error:
            print(f'Info not loading {Error}')


def get_seed_info(connect):
    with connect:
        try:
            return connect.execute(LIST_INFO).fetchall()
        except Error:
            print(f'Not getting information for seeds due to {Error}')


def get_seed_info_by_name(connect, name):
    with connect:
        try:
            return connect.execute(SEED_BY_NAME, (name, )).fetchall()
        except Error:
            print(f'Not getting information for seeds due to {Error}')


def get_seed_info_by_type(connect, seed_type):
    with connect:
        try:
            return connect.execute(SEED_BY_TYPE, (seed_type, )).fetchall()
        except Error:
            print(f'Not getting information for seeds due to {Error}')
