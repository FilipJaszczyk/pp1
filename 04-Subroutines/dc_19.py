def suma(n):
    if n > 0:
        return n + suma(n-1)
    return 0
print(suma(500))