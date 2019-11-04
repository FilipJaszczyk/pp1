from random import randint 
def rzucKostka():
    rzut = randint(1,6)
    return rzut
oczko = 0
suma = 0
for i in range(3):
    oczko = rzucKostka()
    suma += oczko
    print(oczko,end=' ')
print(f'Suma: {suma}')