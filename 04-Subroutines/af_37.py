print('Podaj kolejne elementy tablicy')
tab = []
for i in range(10):
    i = int(input(''))
    tab.append(i)
def powtarzane(arr):
    for i in tab:
        x = arr.count(i)
        if x == 1:
            print(i,end='   ')
powtarzane(tab)    
