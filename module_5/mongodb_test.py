# Joshua Hammerling
# Assignment 5.2

import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.kqclnov.mongodb.net/?retryWrites=true&w=majority")
db = client.pytech
collection = db.students
print("\n -- Pytech Collection List --")
print(db.list_collection_names())


input("\n\n  End of program, press any key to exit... ")

