from random import randint
#Generating number
x = randint(1,6)
#Collect user input
y = int(input('Podaj, ile oczek kostki wyrzucił komputer: ...'))
#PC result
print(f'Komputer wyrzucił: {x}')
#Comparsion
if x == y:
    message = True
else:
    message = False
print(f'Zgadłeś {message}')