# Day 9: Exercises level 1

# 1
print()

user_age = int(input('Enter your age: '))

if user_age >= 18:
    print('You are old enough to drive')
else:
    print('You need', 18 - user_age, 'more years to drive')

# 2
print()

my_age = 31
your_age = int(input('Enter your age: '))

if your_age > my_age:
    print('You are', your_age - my_age, 'older than me')
elif your_age < my_age:
    print('I am', my_age - your_age, 'older than you')
else:
    print('We have the same age')

# 3
print()

number_one = int(input('Enter the first number: '))
number_two = int(input('Enter the second number: '))

if number_one > number_two:
    print(number_one, 'is grater than', number_two)
elif number_one < number_two:
    print(number_one, 'is smaller than', number_two)
else:
    print('Both numbers are equal')