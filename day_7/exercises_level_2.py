# Day 7: Exercises level 2

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print()
print(A)
print(B)

# 1

union_set = A.union(B)
print('The union of A with B is:', union_set)
print()

# 2

intersection_set = A.intersection(B)
print('The insersection of A with B is:', intersection_set)
print()

# 3

print('Is A a subset of B?:', A.issubset(B))
print()

# 4

print('Are A a and B disjoint sets?:', A.isdisjoint(B))
print()

# 5 -> trivial

# 6

symmetric_difference = A.symmetric_difference(B)
print('The symmetric difference between A and B is:', symmetric_difference)
print()

# 7 

del A
del B
