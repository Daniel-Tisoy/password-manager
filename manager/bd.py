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
        sql_query = 'CREATE TABLE passwords (site VARCHAR(100), username VARCHAR(50),password VARCHAR(50))'

        self.run_query(sql_query)

    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def get_by_id(self):
        pass

    def get_all(self):
        pass
