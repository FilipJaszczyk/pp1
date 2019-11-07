from random import randint

def percentage():
    even = 0
    odd = 0
    for x in range(1,1001):
        x = randint(1,50)
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"Liczb parzystych: {(even/1000)*100}%")
    print(f"Liczb nieparzystych: {(odd/1000)*100}%")
    
percentage()
