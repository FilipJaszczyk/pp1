tab = []
numbers = 0
suma = 0 
with open('numbersinrows.txt','r') as file:
    for line in file:
        #zmienia każdą linijkę w listę po czym liczy jej elementy i dodaje do ogółu
        new_line = line.split(',')
        #print(new_line) 
        numbers += len(new_line)
        #print(numbers)
        #dodaje kolenje wartosci w listach
        for i in new_line:
            suma += int(i)
            #print(suma)
file.close
print(f'Liczb w pliku: {numbers}\nSuma liczb w pliku: {suma}')
