from math import pi
print('Calculate area and circuit')
#User input
radius = float(input('Enter radius: '))
#Calculations
area = radius**2*pi
circuit = 2*radius*pi 
#Show result
print(f'Area is equal to {area}\nCircuit is equal to {circuit}')

