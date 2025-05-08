# 1. Use lambda with dictionary comprehension to map names to name lengths
#don't need lambda technically can't it just be Len(x)?
names = ['david', 'lila', 'miriam', 'chana']
name_lengths = {
    name: (lambda x: len(x))(name) for name in names
}
print("Name lengths:", name_lengths)

# 2. Filter a list to keep only numbers divisible by 3
# also don't need lambda though
numbers = list(range(1, 20))
divisible_by_3 = list(
    (filter(lambda x: x % 3 == 0, numbers))
)

print("Divisible by 3:", divisible_by_3)

# 3. Filter a dictionary to keep only values > 75
scores = {'Eli': 88, 'Sara': 74, 'Mo': 91, 'Rachel': 68}
#You don't need a lambda though this could be just a basic if statement????
high_scores = {k: v for k, v in scores.items() if (lambda score: score >75)(v) }
print("High scores:", high_scores)

# 4. Sort a list of (name, age) tuples by age
people = [('Eli', 28), ('Sara', 21), ('Mo', 35), ('Rachel', 25)]
sorted_people = sorted(
    people, key = lambda x: x[1]
)

print("Sorted people by age:", sorted_people)

# 5. Sort dictionary entries by value (descending)
grades = {'Eli': 88, 'Sara': 74, 'Mo': 91, 'Rachel': 68}
sorted_grades = dict(
    sorted(grades.items(), key = lambda x: x[1], reverse = True)
)

print("Grades sorted:", sorted_grades)

