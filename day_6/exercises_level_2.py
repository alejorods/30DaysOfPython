# Day 6: Exercises level 2

# 1

fruits = ('Banana', 'Strawberry', 'Orange', 'Apple')
vegetables = ('Carrot', 'Tomato', 'Celery')
animal_products = ('Milk', 'Cheese', 'Ham')

food_stuff_tp = fruits + vegetables + animal_products

# 2

food_stuff_lt = list(food_stuff_tp)

# 3

length_fs_lt = len(food_stuff_lt) / 2
n = int(length_fs_lt)
middle_item_fs_lt = food_stuff_lt[n-1:n+1]

# 4

first_three_fs_lt = food_stuff_lt[0:3]
last_three_fs_lt = food_stuff_lt[-3:]

# 5 

del food_stuff_tp

# 6 

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print()
print('Is Estonia a nordic country?:', 'Estonia' in nordic_countries)
print('Is Iceland a nordic country?:', 'Iceland' in nordic_countries)
