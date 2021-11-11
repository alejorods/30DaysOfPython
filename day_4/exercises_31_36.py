# Day 4: Exercises 31 - 36.

# 31

print()
print('Which one of the following variables return True when we use the method isidentifier():')
print('\'30DaysOfPython\':', '30DaysOfPython'.isidentifier())
print('\'thirty_days_of_python\':', 'thirty_days_of_python'.isidentifier())
print()  

# 32

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
lib_string = ' # '.join(libraries)
print(lib_string)
print()  

# 33

print('I am enjoying this challenge.\nI just wonder what is next.')
print()

# 34

print('Name\t\tAge\tCountry\t\tCity')
print('Alejandro\t31\tArgentina\tBuenos Aires')
print()

# 35

radius = 10
area = 3.14 * radius**2
print('The area of a circle with radius {} is {} meters square.'.format(radius, int(area)))
print()  

# 36

a = 8
b = 6   
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {round(a / b, 2)}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')