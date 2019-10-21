tab = [15, 8, 31, 47, 2, 19]
#counter zlicza libczę nieparzystych elementów w tablicy
#suma oznacza sumę wszystkich nieparzystych elementów w tablicy
suma = 0
counter = 0
for i in tab:
    if i%2 == 1:
        suma += i
        counter +=1 
    else:
        continue
print(f'{suma/counter}')