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

    # Student ID to delete
    student_id_to_delete = "0942304"

    # Find the student record before deletion
    original_record = student_collection.find_one({"student_id": student_id_to_delete})
    print("Student record before deletion:")
    pprint.pprint(original_record)

    # Write an expression that deletes the student record.
    result = student_collection.delete_one({"student_id": student_id_to_delete})
    print(f"Student record deleted for ID {student_id_to_delete}: {result.deleted_count} record(s)")

    # Attempt to find the student record after deletion
    deleted_record = student_collection.find_one({"student_id": student_id_to_delete})
    if deleted_record:
        print("Student record still exists after deletion.")
    else:
        print("Student record successfully deleted.")

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
