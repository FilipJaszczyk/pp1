import re
suma = 0
with open('land.txt', 'r') as file:
     x = file.read()
     numbers = re.findall('[0-9]',x)
     for i in numbers:
         suma += int(i)
     print(numbers)
     print(suma)
file.close