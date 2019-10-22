pesel = input('Podaj pesel: ')
age = 2019 - int(pesel[:2]) - 1900
print(f'Wiek: {age}')
if int(pesel[9]) % 2 == 0:
    print('Płeć: żeńska')
else:
    print('Płęć: męska')
    