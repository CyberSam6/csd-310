from pymongo import MongoClient

def printRow(student):
    print(f"Student ID: {student['student_id']}\nFirst Name: {student['first_name']}\nLast Name: {student['last_name']}")
    print()

def printAll():
    elements = students.find({})
    for student in elements:
        printRow(student)

url = "mongodb+srv://admin:admin@atlascluster.x1bihsw.mongodb.net/pytech"
client = MongoClient(url)
students = client.pytech.students

print('--- Original Content ---')
printAll()

new = {"student_id": 1010, "first_name": "Jack", "last_name": "Black"}
students.insert_one(new)

print('--- New Row ---')
student = students.find_one({"student_id": 1010})
printRow(student)
students.delete_one({"student_id": 1010})

print('--- New Content ---')
printAll()