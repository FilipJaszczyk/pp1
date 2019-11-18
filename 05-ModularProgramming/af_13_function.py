string_test = 'jAn noWAK'

def znakiWspak(string):
    print(string[::-1])

#znakiWspak(string_test)

def sepratedByspace(string):
    print(' '.join(string))

#sepratedByspace(string_test)

def upperletters(string):
    arr = string.split(' ')
    for i in arr:
        print(i.capitalize(),end=' ')
    
#upperletters(string_test)