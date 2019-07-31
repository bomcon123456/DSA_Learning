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

    def get_owned_books_lists(self):
        pipeline = [
            {"$match": {"_id": self._id}},
            {"$project": {"_id": 0, "ownedBooks.id": 1}},
            {"$unwind": "$ownedBooks"},
            {"$project": {"id": "$ownedBooks.id"}},
        ]
        result = []
        response = self._mongoDB.aggregate(pipeline)
        for each in response:
            result.append(each["id"])
        return result

    def purchase_book(self, book, price):
        self.ownedBooks.append({"id": book["_id"], "page": 0})
        self.wallet -= price
        self._mongoDB.update_one(
            {"username": self.username},
            {
                "$push": {"ownedBooks": {"id": book["_id"], "currentPage": 0}},
                "$set": {"wallet": self.wallet},
            },
        )

    def set_current_page(self, bookId, currentPage):
        for index, each in enumerate(self.ownedBooks, start=0):
            if each["id"] == bookId:
                object = {"id": each["id"], "currentPage": currentPage}
                self.ownedBooks[index] = object
        print(self.ownedBooks)

        self._mongoDB.update_one(
            {"username": self.username}, {"$set": {"ownedBooks": self.ownedBooks}}
        )

    def get_username(self):
        return self.username
