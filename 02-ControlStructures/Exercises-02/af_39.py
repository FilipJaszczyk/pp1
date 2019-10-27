a, b = 0, 1
for i in range(1,51):
    a, b = b, a+b
    print(b)
