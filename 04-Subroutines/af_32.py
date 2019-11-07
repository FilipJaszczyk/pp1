arr = [[1, 2, 0], [0, 0, 3], [5, 1, 1]]


def transpozycja(macierz):
    #wyświetla macierz
    print('Macierz: ')
    for i in macierz:
        print('\n')
        for j in i:
            print(j, end='')
    print('\nMacierz transponowana: ')
    #transponuje daną macierz
    for j in range(len(macierz)):
        print('\n')
        for i in macierz:
            print(i[j], end='')


transpozycja(arr)
