from pymongo import MongoClient
import pprint

# Connect to MongoDB (replace with your actual MongoDB URI)
uri = "mongodb+srv://puttasathvik16:Sathvik123@cluster0.4xuta2y.mongodb.net/"
client = MongoClient(uri)

try:
    # Get reference to 'student_finances' database
    db = client.student_finances

    # Get reference to 'expense_records' collection
    expenses_collection = db.expense_records

    # Filter: Select all expenses related to food
    select_food_expenses = {"category": "Food"}

    # Update: Set a minimum budget for food expenses
    set_min_food_budget = {"$set": {"budget_limit": 200}}

    # Print original expense record
    original_expense = expenses_collection.find_one(select_food_expenses)
    pprint.pprint(original_expense)

    # Write an expression that sets a minimum budget for food expenses.
    result = expenses_collection.update_many(select_food_expenses, set_min_food_budget)
    print(f"Food expenses updated: {result.modified_count} records")

    # Print updated expense record
    updated_expense = expenses_collection.find_one(select_food_expenses)
    pprint.pprint(updated_expense)

except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()
