from pymongo import MongoClient
url = "mongodb+srv://admin:admin@atlascluster.x1bihsw.mongodb.net/pytech"
client = MongoClient(url)
students = client.pytech.students

jon = {"student_id": 1007, "first_name": "Jon", "last_name": "smith"}
freddy = {"student_id": 1008, "first_name": "freddy", "last_name": "lucas"}
cameron = {"student_id": 1009, "first_name": "Cameron", "last_name": "rob"}

jon_student_id = students.insert_one(jon).inserted_id
freddy_student_id = students.insert_one(freddy).inserted_id
cameron_student_id = students.insert_one(cameron).inserted_id
elements = students.find({})
for ele in elements:
  print(ele)
print(students.find_one({"student_id": 1007})) 