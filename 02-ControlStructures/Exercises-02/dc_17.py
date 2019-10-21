even = 0
odd = 0
for i in range(51):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print(f'Suma parzystych ={even} Suma nieparzystych ={odd}')