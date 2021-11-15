# Day 10: Exercises level 1

# 1
print()

list_11 = []
for i in range(11):
    list_11.append(i)
print(list_11)

list_12 = []
n = 0
while n < 11:
    list_12.append(n)
    n += 1
print(list_12)

# 2
print()

list_21 = []
for i in range(10,-1,-1):
    list_21.append(i)
print(list_21)

list_22 = []
n = 10
while n >= 0:
    list_22.append(n)
    n -= 1
print(list_22)

# 3
print()

for i in range(7):
    print('#' * (i + 1))

# 4
print()

for i in range(8):
    print('# ' * 8)

# 5
print()

for i in range(11):
    print(f'{i} x {i} = {i * i}')

# 6
print()

list_6 = ['Python', 'Numpy','Pandas','Django', 'Flask']

for item in list_6:
    print(item)

# 7
print()

list_7 = []

for i in range(101):
    if i % 2 == 0:
        list_7.append(i)
print(list_7)

# 8
print()

list_8 = []

for i in range(101):
    if i % 2 != 0:
        list_8.append(i)
print(list_8)