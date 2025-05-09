
student_data = {
    101: {"name": "Alice", "grades": [85, 90, 88, 92], "gpa": round(sum([85, 90, 88, 92]) / len([85, 90, 88, 92]) / 25, 2)},
    102: {"name": "Bob", "grades": [78, 82, 80, 75], "gpa": round(sum([78, 82, 80, 75]) / len([78, 82, 80, 75]) / 25, 2)},
    103: {"name": "Charlie", "grades": [95, 88, 92, 90], "gpa": round(sum([95, 88, 92, 90]) / len([95, 88, 92, 90]) / 25, 2)}
}

for student_id, data in student_data.items():
    print(f"Student ID: {student_id}")
    print(f"Name: {data['name']}")
    print("Grades:", data['grades'])
    print(f"GPA: {data['gpa']}\n")

