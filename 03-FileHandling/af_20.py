tab = []
with open('numbers.txt', 'r') as file: 
    for line in file:
        if int(line) % 2 == 0:
            tab.append(int(line))
file.close
with open('evennumbers.txt', 'a') as file:
    for i in tab:
        file.write(str(i) + '\n')
file.close