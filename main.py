from manager.bd import Db

def show_menu():
    print("   W E L C O M E   ")
    print("password manager by dtisoy")
    menu = input('''
                    [n]ew user
                    [l]ist passwords 
                    [s]earch
                    [u]pdate
                    [d]elete
                    [q]uit
                    ''').lower()
    if menu == 'q':
        print(r'see you :)')
        exit()
    if menu == 'n':
        add_pass()
    elif menu =="l":
        get_all_pass()
    elif menu == "s":
        get_pass()
    elif menu == 'u':
        update_pass()
    elif menu == "d":
        delete_pass()
    
def add_pass():
    pass


def update_pass():
    pass


def delete_pass():
    pass


def get_pass():
    # get pass using like sql statement
    pass


def get_all_pass():
    pass
if __name__ == "__main__":
    # get the db
    my_passwords_db = Db(".danielPasswords")
    # show the menu
    show_menu()
