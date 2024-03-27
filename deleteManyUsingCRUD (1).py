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

    # Filter: Select records with low balances (outdated or irrelevant)
    select_low_balance_records = {"balance": {"$lt": 2000}}

    # Print original record before deletion
    original_record = student_collection.find_one(select_low_balance_records)
    print("Student record before deletion:")
    pprint.pprint(original_record)

    # Write an expression that deletes the low-balance records.
    result = student_collection.delete_many(select_low_balance_records)
    print(f"Student records deleted: {result.deleted_count} records")

    # Attempt to find the record after deletion
    deleted_record = student_collection.find_one(select_low_balance_records)
    if deleted_record:
        print("Student record still exists after deletion.")
    else:
        print("Student records successfully deleted.")

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
