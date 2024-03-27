from pymongo import MongoClient
import pprint

# Connect to MongoDB (replace with your actual MongoDB URI)
uri = "mongodb+srv://puttasathvik16:Sathvik123@cluster0.4xuta2y.mongodb.net/"
client = MongoClient(uri)

try:
    # Get reference to 'scholarships' database
    db = client.scholarships

    # Get reference to 'student_scholarships' collection
    scholarships_collection = db.student_scholarships

    # Find scholarships for eligible students
    eligible_students_query = {"gpa": {"$gte": 3.5}}

    # Retrieve scholarships matching the eligibility criteria
    cursor = scholarships_collection.find(eligible_students_query)

    num_scholarships = 0
    for scholarship in cursor:
        num_scholarships += 1
        pprint.pprint(scholarship)
        print()

    print(f"Total scholarships found: {num_scholarships}")

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
