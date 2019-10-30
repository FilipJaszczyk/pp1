tab = []
sum0 = 0
with open('numbers.txt','r') as file:
    for line in file:
        tab.append(int(line))
    for i in tab:
        sum0 += i 
    print(sum0)
file.closed