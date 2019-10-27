from random import randint
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
for i in range(100):
    i = randint(1,6)
    if i == 1:
       counter1 += 1
    elif i == 2:
       counter2 += 1
    elif i == 3:
       counter3 += 1
    elif i == 4:
        counter4 += 1
    elif i == 5:
        counter5 += 1 
    elif i == 6:
        counter6 += 1 
print(counter1)
print(counter2)
print(counter3)
print(counter4)
print(counter5)
print(counter6)