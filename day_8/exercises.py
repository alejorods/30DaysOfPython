# Day 8: Exercises

# 1

dog = {}

# 2

dog['name'] = 'Keisha'
dog['color'] = 'Golden'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 12

# 3

student = {}

student['first_name'] = 'Alejandro'
student['last_name'] = 'Rodriguez'
student['gender'] = 'Male'
student['age'] = 31
student['skills'] = ['Math', 'Python', 'Latex']
student['country'] = 'Argentina'
student['city'] = 'Buenos Aires'

# 4

print()
student_length = len(student)
print('The length of the dictionary is', student_length)
print()

# 5

print(student['skills'])
print(type(student['skills']))
print()

# 6

student['skills'].append('Quick learning')
student['skills'].append('UNIX')

# 7

print(student.keys())
print()

# 8 

print(student.values())
print()

# 9

print(student.items())
print()

# 10

student.pop('gender')

# 11

del dog
del student
