# Day 2: 30 Days of Python programming.

# Exercises: Level 1

print('\n1 Declaring variables')

first_name = 'Alejandro'
last_name = 'Rodríguez'
full_name = 'Alejandro Rodríguez'
country = 'Argentina'
city = 'Buenos Aires'
age = 31
year = 2021
is_married = True
is_true = True
is_light_on = False 
current_country, current_city, current_month, current_year = 'Germany', 'München', 'november', 2021

# Exercises: Level 2

print('\n2.1 Built-in functions: type()')

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(current_country))
print(type(current_city))
print(type(current_month))
print(type(current_year))

print('\n2.2 Built-in functions: lenght()')

lenght_first_name = len(first_name)
print('My first name has', lenght_first_name, 'letters.')
lenght_last_name = len(last_name)
print('My last name has', lenght_last_name, 'letters.')

# print('\n2.3 Operations with variables')

num_one = 5
num_two = 4

total = num_one + num_two
variable_diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one**num_two
floor_division = num_one // num_two

print('\n2.4 Radius exercise')

radius = 30
pi = 3.14   # Approximation of number pi
area_of_circle = pi * radius**2
circum_of_circle = 2 * pi * radius
print('The area of a circle of radius = 30 meters is', area_of_circle, 'square meters,')
print('and its circumference is', circum_of_circle, 'meters.')

user_radius = int(input('What is the radius of the circle in meters?: '))
area_of_user_circle = pi * user_radius**2
circum_of_user_circle = 2 * pi * user_radius
print('The area of a circle of radius =', user_radius, 'meters is', area_of_user_circle, 'square meters,')
print('and its circumference is', circum_of_user_circle, 'meters.')

print('\n2.5 Built-in functions: input()')

user_first_name = input('What is your first name?: ')
user_last_name = input('What is your last name?: ')
user_country = input('Where are you from?: ')
user_age = int(input('What is your age?: '))