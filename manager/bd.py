""" this file is for manage the database with passwords"""
import sqlite3


class Db:
    """
    - db queries, add, delete, get, update for a basic database
    - create db tables
    """

    def __init__(self, db_name):
        self.db_name = db_name

    def run_query(self, query, data=()):
        """Run SQL queries with sqlite3 library

        Args:
            query (str): SQL query string
            data (tuple, optional): if the sql need values, add them here. Defaults to ().

        Returns:
            Object: Object sqlite3 cursor
        """
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            result = cursor.execute(query, data)
            connection.commit()

        return result

    def create_table(self):
        """create the table passwords in the db
        """
        sql_query = '''CREATE TABLE passwords (id INTEGER PRIMARY KEY,
            site VARCHAR(100), 
            username VARCHAR(50), 
            password VARCHAR(50))'''

        self.run_query(sql_query)

    def add(self, site, username, password):
        """add a new row in the passwords db

        Args:
            site (str): website domain
            username (str): your website account username or mail
            password (str): your password
        """
        sql_query = 'INSERT INTO passwords(site, username, password) VALUES (?, ?, ?)'
        data = (site, username, password)
        self.run_query(sql_query, data)

    def update(self, db_column, data):
        """update a record through the id,
        database fields: site, username, password

        Args:
            db_column (str): db fields string
            data (tuple): send (new_column_value, id)
        """
        sql_query = f'UPDATE passwords SET {db_column} = ? WHERE id = ?'
        self.run_query(sql_query, data)

    def delete(self, unique_key):
        """delete a record through its id

        Args:
            unique_key (int): its the id of the row
        """
        sql_query = f'DELETE FROM passwords WHERE id = {unique_key}'
        self.run_query(sql_query)

    def get_by_id(self, unique_key):
        """get one record from the db through its id

        Args:
            unique_key (int):  id of the row

        Returns:
            tuple: (id, site, username, password)
        """
        sql_query = f'SELECT * FROM passwords WHERE id = {unique_key}'
        data = self.run_query(sql_query)
        return data.fetchone()

    def get_all(self):
        """get all of the passwords records in the db

        Returns:
            list: [(site, username, password)]
        """
        sql_query = 'SELECT * FROM passwords'
        password_records = (self.run_query(sql_query)).fetchall()
        return password_records
