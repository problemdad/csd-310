# Joshua Hammerling
# Assignment 5.2 - Queries

# START PROGRAM

# Import

import pymongo
from pymongo import MongoClient

# Define the client

client = MongoClient("mongodb+srv://admin:admin@cluster0.kqclnov.mongodb.net/?retryWrites=true&w=majority")

# Define db variable

db = client.pytech

# Define the students collection 
students = db.students

# Find all students in the collection 
student_list = students.find({})

# Display mandatory message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# For loop of the collection and output results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Find document by student_id
bilbo = students.find_one({"student_id": "1008"})

# Display the find_one reults
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + bilbo["student_id"] + "\n  First Name: " + bilbo["first_name"] + "\n  Last Name: " + bilbo["last_name"] + "\n")

# Display mandatory outro message
input("\n\n  End of program, press any key to continue...")

# END PROGRAM