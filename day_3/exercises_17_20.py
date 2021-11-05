# Day 3: Exercises 17 - 20

#17

print()
number = int(input('Enter an integer number: '))
is_even = (number % 2) == 0
print('Is', number, 'even?:', is_even)
print()

#18

check_1 = (7 // 3) == int(2.7)
print("Is (7 // 3) equal to int(2.7)?:", check_1)
print()

#19

check_2 = type('10') == type(10)
print("Is type('10') equal to type(10)?:", check_2)
print()

#20. If we take '9.8' as in the statement, the result is an error,
#because int() doesn't admit strings as arguments.

check_3 = int(9.8) == 10
print("Is int(9.8) equal to 10?:", check_3)