import sqlite3
from sqlite3 import Error


def initialize_database():
    try:
        conn = sqlite3.connect('/Users/jaridley/Database/seed_catalog.db')
        return conn
    except Error:
        print(Error)


def create_seed_table(conn):
    with conn:
        try:
            conn.execute()
        except Error:
            print(Error)


def insert_seed_info(conn):
    with conn:
        try:
            conn.execute()
        except Error:
            print(Error)


def add_seed_info(conn):
    with conn:
        try:
            conn.execute()
        except Error:
            print(Error)


def get_all_seed_info(conn):
    with conn:
        try:
            conn.execute()
        except Error:
            print(Error)
