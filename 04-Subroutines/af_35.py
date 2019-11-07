def digitNumber(n):
    if n >= 0 and n <= 9:
        return 1
    else:
         return 1 + digitNumber(n // 10)
x  = int(input('Enter a natural number: '))
print(digitNumber(x))