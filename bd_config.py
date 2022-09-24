"""this file is for create the db for the first time
just execute this file one time!"""
from manager.bd import Db


def create_db():
    """create_db() -> db file with password table
    """
    new_db = Db(".danielPasswords")
    new_db.create_table()


if __name__ == "__main__":
    create_db()
