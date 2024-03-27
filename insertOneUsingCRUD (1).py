from pymongo import MongoClient
import datetime

# Connect to MongoDB (replace with your actual MongoDB URI)
uri = "mongodb+srv://puttasathvik16:Sathvik123@cluster0.4xuta2y.mongodb.net/"
client = MongoClient(uri)

try:
    # Get reference to 'students' database
    db = client.students

    # Get reference to 'student_records' collection
    student_collection = db.student_records

    # Create a new student record
    new_student = {
        "student_id": "0942304",
        "full_name": "Sathvik Putta",
        "courses": ["ADV Database Design", "Big Data", "Scripting"],
        "assignments": {
            "ADV Database Design": {"assignment1": 90, "assignment2": 85},
            "Big Data": {"assignment1": 78, "assignment2": 92},
            "Scripting": {"assignment1": 95}
        },
        "last_updated": datetime.datetime.utcnow(),
    }

    # Insert the 'new_student' document into the 'student_records' collection
    result = student_collection.insert_one(new_student)

    document_id = result.inserted_id
    print(f"New student record created with ID: {document_id}")

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()




