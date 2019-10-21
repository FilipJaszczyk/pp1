x = int(input('x: '))
y = int(input('y: '))
if x > 0 and y > 0:
    print('1cw')
elif x > 0 and y < 0:
    print('4cw')
elif x < 0 and y > 0:
    print('2cw')
elif x < 0 and y < 0:
    print ('3cw')
elif x == 0 and y != 0:
    print('na osi Y')
elif y == 0 and x !=0:
    print('na osi X')
elif x == 0 and y == 0:
    print('srodek ukladu')