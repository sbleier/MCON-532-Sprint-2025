
import unittest

students_data = {
    101: {"name": "Alice", "grades": [85, 90, 88], "gpa": round(sum([85, 90, 88]) / len([85, 90, 88]) / 25, 2)},
    102: {"name": "Bob", "grades": [78, 82, 80], "gpa": round(sum([78, 82, 80]) / len([78, 82, 80]) / 25, 2)},
    103: {"name": "Charlie", "grades": [92, 88, 95], "gpa": round(sum([92, 88, 95]) / len([92, 88, 95]) / 25, 2)}
}

class TestStudentData(unittest.TestCase):

    def test_number_of_students(self):
        self.assertEqual(len(students_data), 3)

    def test_student_keys(self):
        for student_id, student_info in students_data.items():
            self.assertIn("name", student_info)
            self.assertIn("grades", student_info)
            self.assertIn("gpa", student_info)

    def test_grades_type(self):
        for student_id, student_info in students_data.items():
            self.assertTrue(all(isinstance(grade, int) for grade in student_info["grades"]))

if __name__ == '__main__':
    unittest.main()

