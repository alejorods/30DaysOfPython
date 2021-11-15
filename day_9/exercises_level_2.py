# Day 9: Exercises level 2

# 1
print()

score = int(input('Enter the student score: '))

if score > 100 or score < 0:
    print('This is not a valid score')
elif score < 50:
    print('The grade is F')
elif score < 60:
    print('The grade is D')
elif score < 70:
    print('The grade is C')
elif score < 90:
    print('The grade is B')
else:
    print('The score is A')

# 2
print()

month = input('What month we are?: ').lower()


if month == 'september' or month == 'october' or month == 'november':
    print('The season is Autumm')
elif month == 'december' or month == 'january' or month == 'february':
    print('The season is Winter')
elif month == 'march' or month == 'april' or month == 'may':
    print('The season is Spring')
elif month == 'june' or month == 'july' or month == 'august':
    print('The season is Summer')

# 3
print()

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
print()

new_fruit = input('Add a fruit to the list: ').lower()

if new_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(new_fruit)
    print(fruits)




