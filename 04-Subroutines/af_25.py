names = ['Adam', 'Wojtek', 'Paweł']
name = input('Podaj imię: ')
def nameChecker (names, name):
    print(names)
    print(name)
    if name in names:
        print('Rezultat: imię zawarte w tablicy')
    else:
        print('Rezultat: imię nie zawarte w tablicy')
nameChecker(names,name)