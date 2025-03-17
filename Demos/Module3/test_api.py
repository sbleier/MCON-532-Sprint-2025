from src.open_api_client import get_openai_client
from pprint import pprint

client = get_openai_client()
pprint(vars(client))

# Make a request to OpenAI API
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user" "content": "Create a Python dictionary where each student ID maps to another dictionary containing:"
        "'name': Student’s name (string)"
        "'grades: A list of grades (integers)."
        "'gpa: The GPA, calculated as (sum of grades / number of grades) / 25, rounded to two decimal places."
        "Use dictionary comprehension, and then format the output using print() so that the student data is displayed in a well-structured format."}
    ]
)



# Output the response
pprint(completion)
pprint(completion.choices[0].message.content)