tab = []
n =int(input('Liczb pierwszych: '))
i = 2
while len(tab) < n-1:
    isFirst = True
    for a in tab:
        if i % a == 0:
            isFirst = False
            break
    if isFirst == True:
        tab.append(i)
    i += 1
tab.insert(0,1)
print(tab)
