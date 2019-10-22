names = ['zero', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']
number = input('Podaj liczbe: ')
print(number, end = ' - ')
for i in number:
    print(names[int(i)], end = ' ')    