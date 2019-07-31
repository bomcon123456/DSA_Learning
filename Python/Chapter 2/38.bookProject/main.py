from pymongo import MongoClient
from gui import GUI
from user import User

client = MongoClient("mongodb+srv://test:test@cloud-ejl26.mongodb.net/")

db = client["python"]
# Users = db["users"]
# User.aggregate()

mainProgram = GUI(db)

# mainProgram._user = User(
#     Users.find_one({"username": "admin", "password": "admin"}), Users
# )
mainProgram.welcome()

