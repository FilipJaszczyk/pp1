user_input = 1
counter = 0
suma = 0
while user_input != 0:
    user_input = int(input('Podaj liczbę: '))
    if user_input == 0:
        print(f'Liczba liczb: {counter}\nSuma liczb: {suma}\nŚrednia arytmetyczna: {suma/counter}')
        break
    counter += 1
    suma += user_input
    '''print(user_input)
    print(counter)
    print(suma)'''