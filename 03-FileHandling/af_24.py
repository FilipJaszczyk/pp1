tab = [['Marek', 'Zelnik', 'zelnik@sed.pl'], [
    'Ewa', 'Maj', 'maje@wp.pl'], ['Piotr', 'Wyga', 'wygap@gop.pl']]
with open('csv_data.csv', 'w') as file:
    file.write('Imie, Nazwisko, Email\n')
    for i in range(len(tab)):#looping over 1 dimension
        for j in range(len(tab[i])):#loopin over second
            string_value = ','.join(tab[j])
            file.write(f'{string_value}\n')
        #file.write(file_input)
file.close

