from pymongo import MongoClient
from gui import GUI

client = MongoClient("mongodb+srv://test:test@cloud-ejl26.mongodb.net/")

db = client["python"]

mainProgram = GUI(db)

mainProgram.welcome()

