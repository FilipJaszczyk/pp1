tab = []
#put elements to tab
with open('universities.txt', 'r') as file:
    for line in file:
        tab.append(line)
file.close
#overwrite the file with elements from tab 
with open('universities.txt', 'w') as file:
    for i in sorted(tab):
        file.write(i)
file.close
