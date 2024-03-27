from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

# Connect to MongoDB (replace with your actual MongoDB URI)
uri = "mongodb+srv://puttasathvik16:Sathvik123@cluster0.4xuta2y.mongodb.net/"
client = MongoClient(uri)

try:
    # Get reference to 'students' database
    db = client.students

    # Get reference to 'student_rewards' collection
    rewards_collection = db.student_rewards

    # Student ID to update rewards
    student_id_to_update = "0942303"

    # Update rewards by adding bonus points
    add_bonus_points = {"$inc": {"rewards": 50}}

    # Print original rewards
    original_rewards = rewards_collection.find_one({"student_id": student_id_to_update})
    pprint.pprint(original_rewards)

    # Write an expression that adds bonus points to the student's rewards.
    result = rewards_collection.update_one({"student_id": student_id_to_update}, add_bonus_points)
    print(f"Rewards updated for student {student_id_to_update}: {result.modified_count} points added")

    # Print updated rewards
    updated_rewards = rewards_collection.find_one({"student_id": student_id_to_update})
    pprint.pprint(updated_rewards)

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
