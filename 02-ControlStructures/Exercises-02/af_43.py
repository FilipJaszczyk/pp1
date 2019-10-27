tab = []
x = int(input('Podaj pierwszą liczbę: '))
tab.append(x)
y = int(input('Podaj drugą liczbę: '))
tab.append(y)
z = int(input('Podaj trzecią liczbę: '))
tab.append(z)
tab.sort()
#join() Join all items in a tuple into a string, using a ' ' character(only works for strings inside list)
#map(funciton,iterables) str - gives string representation of a object, map executes function for each iterable of a object
print(' '.join(map(str,tab)))
    