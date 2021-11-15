# Day 10: Exercises level 2

# 1
print()

n = 0
for i in range(101):
    n += i 
print('The sum of all numbers from 0 to 100 is', n)

# 2
print()

even_sum = 0
odd_sum = 0

for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i 
print('The sum of all evens from 0 to 100 is', even_sum, 'and the sum of all odds is', odd_sum)