# Joshua Hammerling
# Assignment 6.2

# Import

import pymongo
from pymongo import MongoClient

# Define the client

client = MongoClient("mongodb+srv://admin:admin@cluster0.kqclnov.mongodb.net/?retryWrites=true&w=majority")

# Define db variable

db = client.pytech

# Define student variable

students = db.students

# find all of the students in the collection
student_list = students.find({})


# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# update student 1007 record as required
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

# define updated student record
thorin = students.find_one({"student_id": "1007"})

# display the required record message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output student updated into
print("  Student ID: " + thorin["student_id"] + "\n  First Name: " + thorin["first_name"] + "\n  Last Name: " + thorin["last_name"] + "\n")

# print the exit message

input("\n\n  End of program, press any key to continue...")

# END PROGRAM