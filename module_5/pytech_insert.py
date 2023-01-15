# Joshua Hammerling
# Assignment 5.3 - Insert records


# START PROGRAM

# Import

import pymongo
from pymongo import MongoClient

# Define the client

client = MongoClient("mongodb+srv://admin:admin@cluster0.kqclnov.mongodb.net/?retryWrites=true&w=majority")

# Define db variable

db = client.pytech

# Insert student records

# Thorin Oakenshield's data 
thorin = {
    "student_id": "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield"
}


# Bilbo Baggins data 
bilbo = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins"
}

# Frodo Baggins data 
frodo = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Baggins"
}

# END PROGRAM