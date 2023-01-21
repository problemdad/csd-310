# Joshua Hammerling
# Assignment 6.3


# START PROGRAM

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

# loop the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# generate new student document 
new_kid = {
    "student_id": "1010",
    "first_name": "John",
    "last_name": "Doe"
}

# insert the test document into DB
new_kid_id = students.insert_one(new_kid).inserted_id

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(new_kid_id))

# call the find_one() method by student_id 1010
student_new_kid = students.find_one({"student_id": "1010"})

# display the results 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_new_kid["student_id"] + "\n  First Name: " + student_new_kid["first_name"] + "\n  Last Name: " + student_new_kid["last_name"] + "\n")

# call the delete_one method to remove the student_new_doc
deleted_student_new_kid = students.delete_one({"student_id": "1010"})

# find all students in the collection 
new_student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")


# exit message 
input("\n\n  End of program, press any key to continue...")

# END PROGRAM