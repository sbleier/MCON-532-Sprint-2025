from src.open_api_client import get_openai_client

def send_request(prompt):
  client = get_openai_client()
  response = client.chat.completions.create(
   model="gpt-3.5-turbo",
   messages=[
    {"role": "system", "content": "You are helpful Python assistant"},
    {"role": "user", "content": prompt}
  ],
   temperature=0,
   top_p = 0
  )
  content = response.choices[0].message.content
  print(content)
  return content

def main():
  prompt_one = """Create a Python dictionary where each student ID maps to another dictionary containing:
               "name": Student’s name (string)"
               "grades: A list of grades (integers).
               "gpa": The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places.")"""
  content_one = send_request(prompt_one)

  prompt_two = """Create a Python dictionary where each student ID maps to another dictionary containing:
               "name": Student’s name (string)
               "grades": A list of grades (integers).
               "gpa": The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places.
               Use dictionary comprehension to construct the dictionary."""
  content_two = send_request(prompt_two)

  prompt_three = """Create a Python dictionary where each student ID maps to another dictionary containing:
                 "name": Student’s name (string)
                 "grades": A list of grades (integers).
                 "gpa": The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places.
                 Use dictionary comprehension, and then format the output using print() so that the student data is displayed in a well-structured format.
                 Format response as python file, without superfluous words"""
  content_three = send_request(prompt_three)
  with open("prompt3.py", "w") as file:
   file.write(content_three)

  prompt_four = """Create a Python dictionary where each student ID maps to another dictionary containing:
                "name": Student’s name (string)
                "grades": A list of grades (integers).
                "gpa": The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places.
                Use dictionary comprehension to create it.
                Then, write unit tests using unittest to verify that:
                The dictionary contains the correct number of students.
                Each student has a "name", "grades", and "gpa".
                The "grades" list contains only integers.
                Ensure test coverage using IntelliJ’s built-in coverage tool.
                Format response as python file, without superfluous words"""
  content_four = send_request(prompt_four)

  with open("prompt4.py", "w") as file:
   file.write(content_four)



if __name__ == '__main__':
 main()



# def part1():
#     ('student_dictionary = {\n'
#      "    101: {'name': 'John Doe', 'grades': [85, 90, 88, 92], 'gpa': "
#      'round((sum([85, 90, 88, 92]) / len([85, 90, 88, 92])) / 25, 2)},\n'
#      "    102: {'name': 'Jane Smith', 'grades': [75, 85, 80, 88], 'gpa': "
#      'round((sum([75, 85, 80, 88]) / len([75, 85, 80, 88])) / 25, 2)},\n'
#      "    103: {'name': 'Michael Brown', 'grades': [92, 95, 90, 88], 'gpa': "
#      'round((sum([92, 95, 90, 88]) / len([92, 95, 90, 88])) / 25, 2)}\n'
#      '}\n'
#      '\n'
#      'print(student_dictionary)')
#
# def part2():
#  completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#    {"role": "user" "content": "Create a Python dictionary where each student ID maps to another dictionary containing:"
#                               "'name': Student’s name (string)"
#                               "'grades: A list of grades (integers)."
#                               "'gpa: The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places."
#                               "Use dictionary comprehension, and then format the output using print() so that the student data is displayed in a well-structured format."}
#  ]
#  );
#
# def part3():

