from math import sqrt
print('Enter the sides of triangle')
#user input
a = float(input())
b = float(input())
c = float(input())
#calculation
p = (a+b+c)/2
area = sqrt(p*(p-a)*(p-b)*(p-c))
#result
print(area)