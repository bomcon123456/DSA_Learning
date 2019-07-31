from pymongo import MongoClient
from bson.objectid import ObjectId


class User:
    def __init__(self, user, mongoDB):
        self._id = user["_id"]
        self.fullname = user["fullname"]
        self.username = user["username"]
        self.wallet = user["wallet"]
        self.ownedBooks = user["ownedBooks"]
        self._mongoDB = mongoDB

    def get_owned_books(self):
        return self.ownedBooks

    def purchase_book(self, id):
        self.ownedBooks.append({"id": ObjectId(id), "page": 0})

        self._mongoDB.update_one(
            {"username": self.username},
            {"$push": {"ownedBooks": {"id": ObjectId(id), "currentPage": 0}}},
        )

    def get_username(self):
        return self.username
