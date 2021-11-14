# Day 6: Exercises level 1

# 1

empty_tuple = ()

# 2

brothers = ('Toto',)
sisters = ('Nayi', 'Zhandra')

# 3

siblings = brothers + sisters

# 4

print()
print('How many siblings do you have?')
print('I have', len(siblings), 'siblings.')
print()

# 5

family_members = list(siblings)
family_members.append('Amable')
family_members.append('Nancy')
family_members = tuple(family_members)

# 6 (This is 1 of level 2).

siblings = family_members[0:3]
parents = family_members[-2:]