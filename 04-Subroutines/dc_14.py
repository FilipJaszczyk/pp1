number = 23
tab = [15,38,7,23,14]
def exist(number,tab):
    for i in tab:
        if i == 23:
            print('Podana liczba występuje w tablicy')
print('Liczba: 23')
print(f'Tablica: {tab}')
exist(number, tab)