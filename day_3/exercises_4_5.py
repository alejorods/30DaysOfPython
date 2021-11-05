# Day 3: Exercise 4 and 5

#4

triangle_base = float(input('Enter the base of a triangle: '))
triangle_height = float(input('Enter the height of this triangle: '))

triangle_area = (triangle_base * triangle_height) / 2

print('The area of the triangle is', triangle_area)

#5

side_a = float(input('Enter one side of a triangle: '))
side_b = float(input('Enter another side of this triangle: '))
side_c = float(input('Enter the remaining side of this triangle: '))

triangle_perimeter = side_a + side_b + side_c

print('The perimeter of the triangle is', triangle_perimeter)