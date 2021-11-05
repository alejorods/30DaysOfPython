# Day 3: Exercises 12 - 16

#12

print()
python_lenght = len('python')
print("The length of 'python' is:", python_lenght)
dragon_lenght = len('dragon')
print("The length of 'dragon' is:", dragon_lenght)

print("Are the lenghts of 'python' and 'dragon' different?:", not(python_lenght==dragon_lenght)) #False statement
print()

#13

check_1 = ('on' in 'python') and ('on' in 'dragon')
print("Is 'on' in 'python' and 'dragon'?:", check_1)
print()

#14

sentence = 'I hope this course is not full of jargon'
check_2 = 'jargon' in sentence
print(sentence)
print("Is 'jargon' in this sentence?:", check_2)
print()

#15

check_3 = not check_1
print("There is no 'on' in 'python' and 'dragon'?:", check_3)
print()

#16

print("The length of 'python' is:", python_lenght)
conversion = str(float(python_lenght))
print("The length of 'python' is:", conversion)