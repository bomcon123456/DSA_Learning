import platform  # For getting the operating system name
import subprocess  # For executing a shell command
from user import User


def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "cls" if platform.system().lower() == "windows" else "clear"

    # Action
    return subprocess.call(command) == 0


class GUI:
    def __init__(self, db):
        self._user_mongo = db["users"]
        self._books_mongo = db["books"]
        self._user = None

    def _quit_program(self):
        print("Exiting...")
        quit()

    def _retry_fnc(self, yesFnc, noFnc):
        choose = input("Retry? [y/n]")
        if choose == "y" or choose == "Y":
            yesFnc()
        else:
            noFnc()

    def set_user(self, username):
        self._username = username

    def _welcome_unauth(self):
        print("Welcome to Book Reader.")
        print("1. Login")
        print("2. Exit")
        raw_data = input("Choose: ")
        if raw_data == "1":
            self._login()
            # print("Login")
        elif raw_data == "2":
            self._quit_program()
        else:
            self.welcome()

    def _welcome_auth(self):
        print("Welcome back to Book Reader, {}".format(self._user.get_username()))
        print("1. Go to Bookstore")
        print("2. View Bought Books")
        print("3. Log-out")
        print("4. Exit")
        raw_data = input("Choose: ")
        if raw_data == "1":
            print("Opening Book Store...")
        elif raw_data == "2":
            print("Opening Book List...")
        elif raw_data == "3":
            self._user = None
            self.welcome()
        elif raw_data == "4":
            self._quit_program()
        else:
            self.welcome()

    def _login(self):
        clear_screen()
        print("Login")
        username = input("Username: ")
        password = input("Password: ")
        result = self._user_mongo.find_one({"username": username, "password": password})
        if result == None:
            print("Wrong username/password")
            self._retry_fnc(self._login, self.welcome)
        else:
            self._user = User(result, self._user_mongo)
            print("Login success, taking you back...")
            self.welcome()

    def welcome(self):
        clear_screen()
        if self._user == None:
            self._welcome_unauth()
        else:
            self._welcome_auth()

