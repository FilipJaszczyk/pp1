import csv
import statistics as s 

tab = []
with open('employees.csv','r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        tab.append(row[2])

tab.pop(0)
tab = list(map(int,tab))
print(f'Średnia arytmetyczna: {s.mean(tab)}')
print(f'Mediana: {s.median(tab)}')
print(f'Odchylenie standardowe: {s.stdev(tab)}')
        