import platform  # For getting the operating system name
import subprocess  # For executing a shell command
from pprint import pprint
from user import User
from itertools import islice


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

    def _yes_no_fnc(self, text, yesFnc, noFnc):
        choose = input("{} [y/n]: ".format(text))
        if choose == "y" or choose == "Y":
            yesFnc()
        else:
            noFnc()

    def set_user(self, username):
        self._username = username

    def _handle_purchase(self, book, price):
        self._user.purchase_book(book, price)
        input("Purchase Completed, Back?")
        self.welcome()

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
            self._view_book_list(isStore=True)
        elif raw_data == "2":
            print("Opening Book List...")
            self._view_book_list(isStore=False)
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
            self._yes_no_fnc("Retry ?", self._login, self.welcome)
        else:
            self._user = User(result, self._user_mongo)
            print("Login success, taking you back...")
            self.welcome()

    def _read_at_page(self, src, page):
        count = 0
        with open(src) as f:
            for line in islice(f, page * 25, None):
                if count < 25:
                    print(line)
                    count += 1
                else:
                    break
        f.close()

    def _view_book(self, book, page):
        clear_screen()
        currentPage = int(page) if page > 0 else 1
        self._read_at_page(book["src"], currentPage)
        while currentPage <= int(book["pages"]):
            currentPage += 1
            self._read_at_page(book["src"], currentPage)
            raw_data = input("Next Page/Quit [Enter/q]:")
            if raw_data == "q":
                self._user.set_current_page(book["_id"], currentPage - 1)
                self.welcome()

    def _view_book_details(self, book, fromStore):
        clear_screen()
        print("\t\t{}".format(book["title"]))
        print("Author: {}".format(book["author"]))
        print("Subject: {}".format(book["subject"]))
        print("Description: {}".format(book["description"]))
        print("Page: {}".format(book["pages"]))
        if fromStore:
            print("Price: {}".format(book["price"]))
        print("---------------------------------")
        if fromStore:
            print("Current Wallet: ${}".format(self._user.wallet))
            price = float(book["price"].split("$")[1])
            if price < self._user.wallet:
                self._yes_no_fnc(
                    "Buy ?",
                    lambda: self._handle_purchase(book, price),
                    lambda: self._view_book_list(True),
                )

            else:
                print("You don't have enough money :(")
                input("Back")
                self._view_book_list(True)
        else:
            bookUserInfo = None
            for each in self._user.ownedBooks:
                if each["id"] == book["_id"]:
                    bookUserInfo = each
            if bookUserInfo["currentPage"] == 0:
                print("You haven't read this book yet.")
            else:
                print(
                    "You have read {} pages in this book".format(
                        bookUserInfo["currentPage"]
                    )
                )
            self._yes_no_fnc(
                "Read this book?",
                lambda: self._view_book(book, bookUserInfo["currentPage"]),
                self.welcome,
            )

    def _view_book_list(self, isStore):
        clear_screen()
        user_owned_list = self._user.get_owned_books_lists()
        pipeline = []
        if isStore:
            pipeline.append({"$match": {"_id": {"$nin": user_owned_list}}})
        else:
            pipeline.append({"$match": {"_id": {"$in": user_owned_list}}})
        pipeline.append(
            {
                "$project": {
                    "_id": 1,
                    "description": 1,
                    "pages": 1,
                    "author": 1,
                    "title": 1,
                    "subject": 1,
                    "price": 1,
                    "src": 1,
                }
            }
        )

        result = list(self._books_mongo.aggregate(pipeline))
        for index, i in enumerate(result, start=1):
            print("{}. {}".format(index, i["title"]))
            print("\tAuthor: {}".format(i["author"]))
            print("\tSubject: {}".format(i["subject"]))
            print("\tPage: {}".format(i["pages"]))
            print("\tPrice: {}".format(i["price"]))
        choose = input("View book [0 to back]: ")
        try:
            chooseInt = int(choose)
            print(chooseInt, len(result))
        except (ValueError):
            print("Invalid input.")
            print("Redirecting...")
            self._view_book_list(isStore)
        if chooseInt > len(result):
            print("Invalid input.")
            print("Redirecting...")
            self._view_book_list(isStore)
        elif chooseInt == 0:
            self.welcome()
        else:
            print("Redirecting...")
            self._view_book_details(result[chooseInt - 1], isStore)
        # self.welcome()

    def welcome(self):
        clear_screen()
        if self._user == None:
            self._welcome_unauth()
        else:
            self._welcome_auth()

