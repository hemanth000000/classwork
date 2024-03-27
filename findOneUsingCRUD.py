from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

# Connect to MongoDB (replace with your actual MongoDB URI)
uri = "mongodb+srv://puttasathvik16:Sathvik123@cluster0.4xuta2y.mongodb.net/"
client = MongoClient(uri)

try:
    # Get reference to 'students' database
    db = client.students

    # Get reference to 'student_records' collection
    student_collection = db.student_records

    # Student ID to look up
    student_id_to_find = "0942304"

    # Find the student record by student ID
    student_record = student_collection.find_one({"student_id": student_id_to_find})

    if student_record:
        print(f"Student record for ID {student_id_to_find}:")
        pprint.pprint(student_record)
    else:
        print(f"No student found with ID {student_id_to_find}")

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
