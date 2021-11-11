# Day 4: Exercises 1 - 30.

space = ' '

# 1
print()
concatenation_1 = 'Thirty' + space + 'Days' + space + 'Of' + space +'Python'
print(concatenation_1)
print()

# 2

concatenation_2 = 'Coding' + space + 'For' + space + 'All'
print(concatenation_2)
print()

# 3

company = concatenation_2

# 4 

print(company)
print()

# 5

print('The lenght of \'Coding For All\' is:', len(company))
print()

# 6 

all_uppercase = company.upper()
print(all_uppercase)
print()

# 7

all_lowercase = company.lower()
print(all_lowercase)
print() 

# 8

print('Formating \'Coding For All\':')
print(company.capitalize())
print(company.title())
print(company.swapcase())
print()

# 9

cut_company = company.replace('Coding ', '')
print(cut_company)
print() 

# 10

print('Is \'Coding\' in \'Coding For All\'?:', 'Coding' in company)
print() 

# 11 

new_company = company.replace('Coding', 'Python')
print(new_company)
print()

# 13

split_company = company.split()
print(split_company)
print() 

# 14

it_string = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
it_split = it_string.split(',')
print(it_string)
print(it_split)
print() 

# 15

zero_company = company[0]
print('The character at index zero in \'Coding For All\' is:', zero_company)
print()

# 16

last_index_company = company.rfind('l')
print('The last index of \'Coding For All\' is:', last_index_company)
print()

# 17

ten_company = company[10]
print('The character at index ten in \'Coding For All\' is:', ten_company)
print()

# 18

#acronym = filter(str.isupper, company)
#print('The acronym for \'Coding For All\' is:', acronym)

# 19

# 20

index_C_company = company.index('C')
print('The index of the first ocurrence of \'C\' in \'Coding For All\' is:', index_C_company)
print()

# 21

index_F_company = company.index('F')
print('The index of the first ocurrence of \'F\' in \'Coding For All\' is:', index_F_company)
print()

# 22

index_last_l_company = company.rfind('l')
print('The index of the last ocurrence of \'l\' in \'Coding For All\' is:', index_last_l_company)
print()

# 23

sentence = 'You cannot end a sentence with because because because is a conjunction'

index_because = sentence.index('because')
print('The index of the first ocurrence of \'because\' in \'',sentence,'\' is', index_because)
print()

#24

rindex_because = sentence.rindex('because')
print('The index of the last ocurrence of \'because\' in \'',sentence,'\' is', rindex_because)
print()

# 25

short_sentence = sentence.replace('because because because ', '')
print(short_sentence)
print() 

# 26

find_because = sentence.find('because')
print('The index of the first ocurrence of \'because\' in \'',sentence,'\' is', find_because)
print()

# 27 is repeated. Is exercise 25.

# 28

print('Does \'Coding For All\' start with a substring \'Coding\'?:', company.startswith('Coding'))
print() 

# 29

print('Does \'Coding For All\' end with a substring \'Coding\'?:', company.endswith('Coding'))
print()