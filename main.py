import sqlite3
import getpass
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Consultas:
    db_name = 'passwords'

    def __init__(self):
        try:
            self.open_bbdd()
            logger.info(
                'Se creó la tabla PASSWORDS en {}'.format(self.db_name))
        except:
            logger.info('La base de datos está lista')

    def delete_password(self):
        """Function to delete a record (site, user, password) from the database
        """
        try:
            site = input('sitio web: ')
            query = f'DELETE FROM PASSWORDS WHERE WEB_SITE = "{site}"'
            self.run_query(query)
            logger.info('El registro se ha eliminado correctamente')
        except: 
            logger.warning('Ohh! ha ocurrido un error, tal vez el sitio no existe en la base de datos')

    def update_password(self):
        """function to update a selected user in the data base
        """
        user = self.search_password()
        command = input('''
                            [n]ombre
                            [c]ontraseña
                            ''').lower()
        if command == 'n':
            old_user = user[0][1]
            new_user = input('nuevo usuario: ')
            parameters = (new_user, old_user)
            query = 'UPDATE PASSWORDS SET USER = ? WHERE USER = ?'
            self.run_query(query, parameters)
            self.search_password(user[0][0])
        elif command == 'c':
            old_password = user[0][2]
            new_password = getpass.getpass('nueva contraseña: ')
            parameters = (new_password, old_password)
            query = 'UPDATE PASSWORDS SET PASSWORD = ? WHERE PASSWORD = ?'
            self.run_query(query, parameters)
            self.search_password(user[0][0])
        else:
            logger.warning('Ingrese n o c')
        logger.info('Actualizado con exito :)')

    def search_password(self, site=None):
        """Function to search a record in the data base

        Args:
            site (str, optional): define the web site, if it is None, the funtion will ask you the web site name. Defaults to None.

        Returns:
            list: list of tuples
        """
        if site == None:
            site = input('web site: ')
            query = f'SELECT * FROM PASSWORDS WHERE WEB_SITE = "{site}"'
            user = (self.run_query(query)).fetchall()
            self.print_data(user)
        else:
            query = f'SELECT * FROM PASSWORDS WHERE WEB_SITE = "{site}"'
            user = (self.run_query(query)).fetchall()
            self.print_data(user)
        return user

    def add_password(self):
        """Function to Add new user
        """
        logger.info('añadir nuevos datos')
        web_site = input('Sitio web: ')
        user = input('usuario: ')
        password = getpass.getpass()
        query = 'INSERT INTO PASSWORDS VALUES (?,?,?)'
        parameters = (web_site, user, password)
        self.run_query(query, parameters)
        logger.info(
            'se añadió {} a la base de datos de manera correcta'.format(user))

    def list_table(self):
        """ Function to print all users
        """
        query = 'SELECT * FROM PASSWORDS'
        users = (self.run_query(query)).fetchall()
        self.print_data(users)

    def print_data(self, data=list()):
        """funtion to format the print of users

        Args:
            data (list, optional): a list of tuples. Defaults to list().
        """
        print('-----------------------------------')
        print('SITE         USER        PASSWORD')
        for i in data:
            print('{}   {}  {}'.format(i[0], i[1], i[2]))
        print('-----------------------------------')

    def run_query(self, query, parameters=()):
        """Function to execute database querys

        Args:
            query (string): sql query -> 
            parameters (tuple, optional): parameters of the query. Defaults to ().

        Returns:
            Object: Object cursor
        """
        with sqlite3.connect(self.db_name) as connection:
            logger.info(
                'Conectando a la base de datos {}'.format(self.db_name))
            cursor = connection.cursor()
            result = cursor.execute(query, parameters)
            connection.commit()
        return result

    def open_bbdd(self):
        """Function to create table 'PASSWORDS'
        """
        query = 'CREATE TABLE PASSWORDS (WEB_SITE VARCHAR(50), USER VARCHAR(50),PASSWORD VARCHAR(20))'
        self.run_query(query)


def run():
    print('Bienvenido a pass-world by daniel')
    menu = input('''
                    [n]uevo usuario
                    [l]istar contraseñas
                    [b]uscar
                    [a]ctualizar 
                    [e]liminar
                    [s]alir
                    ''').lower()

    if menu == 's':
        exit()
    else:
        user_pass = Consultas()
        if menu == 'n':
            user_pass.add_password()
        elif menu == 'l':
            user_pass.list_table()
        elif menu == 'b':
            user_pass.search_password()
        elif menu == 'a':
            user_pass.update_password()
        elif menu == 'e':
            user_pass.delete_password()


if __name__ == "__main__":
    run()
