# Day 5: Exercises level 1

# 1

empty_list = []

# 2 

print()
five_item_list = ['One', 2, True, 'four', [1,2,3], 3.14]
print(five_item_list)
print()

# 3

print('The lenght of this list is:', len(five_item_list))
print()

# 4

print('The first item of this list is:', five_item_list[0], '\nthe middle item is:', five_item_list[int((len(five_item_list) - 1) / 2)], '\nand the last item is:', five_item_list[-1])
print()

# 5 

mixed_data_types = ['Alejandro', 31, 1.70, 'married', 'Connollystrasse']

# 6 
 
it_companies = ['Facebook', 'Google', 'Micorsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7

print(it_companies)
print()

# 8

print('The number of companies in this list is:', len(it_companies))
print()

# 9 

print('The first company of this list is:', it_companies[0], '\nthe middle company is:', it_companies[int((len(it_companies) - 1) / 2)], '\nand the last item is:', it_companies[-1])
print()

# 10

it_companies[0] = 'Meta' 
print(it_companies)
print()

# 11

it_companies.append('Twitter')
print(it_companies)
print()

# 12

it_companies.insert(4, 'Globant')
print(it_companies)
print()

# 13

it_companies[-1] = it_companies[-1].upper()
print(it_companies)
print()

# 14

print('#'.join(it_companies))
print()

# 15

print('Is Apple in the list?:', 'Apple' in it_companies)
print('Is Facebook in the list?:', 'Facebook' in it_companies)
print()

# 16

it_companies.sort()
print(it_companies)
print()

# 17

it_companies.reverse()
print(it_companies)
print()

# 18

first_three = it_companies[0:3]
print(first_three)
print()

# 19

last_three = it_companies[-3:]
print(last_three)
print()

# 20

middle_company = [it_companies[int((len(it_companies)-1)/2)]]
print(middle_company)
print()

# 21

it_companies.pop(0)
print(it_companies)
print()

# 22

it_companies.pop(int((len(it_companies)-1)/2))
it_companies.pop(int((len(it_companies)-1)/2))
print(it_companies)
print()

# 23

it_companies.pop(-1)
print(it_companies)
print()

# 24

it_companies.clear()
print(it_companies)
print()

# 25

del it_companies

# 26

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(front_end)
print(back_end)
print(full_stack)
print()

# 27

full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)


