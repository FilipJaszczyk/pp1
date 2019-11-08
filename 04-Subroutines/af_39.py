x = int(input('Podaj górną granice przediału: '))
y = int(input('Podaj dolną granice przedziału: '))
z = int(input('Podaj liczbę :'))

def zakres(x,y,z):
    if z >= y and z <= x:
        print('Mieści się w zakresie')
    else:
        print('Nie mieści się')

zakres(x,y,z) 