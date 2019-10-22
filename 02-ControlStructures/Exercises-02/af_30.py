pinNumber = 8500
for i in range (1,4):
    pin = int(input('Enter PIN: '))
    if pin == pinNumber:
        print('Pin poprawny')
        break
    if pin != pinNumber and  i < 3:
        print('Pin nieprawidłowy')
    if pin != pinNumber and i == 3:
        print('Karta płatnicza zablokowana')