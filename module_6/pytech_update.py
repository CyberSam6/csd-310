from pymongo import MongoClient
url = "mongodb+srv://admin:admin@atlascluster.x1bihsw.mongodb.net/pytech"
client = MongoClient(url)
students = client.pytech.students
students.delete_many({})

jon = {"student_id": 1007, "first_name": "Jon", "last_name": "smith"}
freddy = {"student_id": 1008, "first_name": "freddy", "last_name": "lucas"}
cameron = {"student_id": 1009, "first_name": "Cameron", "last_name": "rob"}

students.insert_many([jon, freddy, cameron])
print('--- Original Content ---')
elements = students.find({})
for student in elements:
    print(f"Student ID: {student['student_id']}\nFirst Name: {student['first_name']}\nLast Name: {student['last_name']}")
    print()
students.update_one({"student_id": 1007}, {"$set": {"last_name": "jeff"}},)
print('--- Updated Row ---')
student = students.find_one({"student_id": 1007})
print(f"Student ID: {student['student_id']}\nFirst Name: {student['first_name']}\nLast Name: {student['last_name']}")