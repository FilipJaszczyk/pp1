tab = ['Genowefa', 'Onufry', 'Celestyna',
       'Alojzy', 'Pankracy', 'Teofil']
counter = []
for i in tab:
    counter.append(len(i)) #dodaje do listy counter długość słów
max_value = max(counter) #szuka najdłuższego słowa
max_value_index = counter.index(max(counter)) #szuka indeksu słowa
print(f'Liter: {max_value} Imię: {tab[max_value_index]}') #wyrzuca indeks słowa z tabeli tab
    
