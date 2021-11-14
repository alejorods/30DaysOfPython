# Day 7: Exercises level 3

print()
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(age)
print()

# 1

age_set = set(age)
length_lt = len(age)
length_st = len(age_set)
print(age_set)
print()
print('The length of the list is', length_lt, 'while the length of the set is', length_st)
print()

# 3

sentence = 'I am a teacher and I love to inspire and teach people'
print(sentence)
print()
print('This sentence has', len(set(sentence.split(' '))), 'unique words.')

