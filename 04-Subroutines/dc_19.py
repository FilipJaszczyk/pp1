n = 500
def suma(n):
    if n >= 1:
        return n + suma(n-1)
print(suma(n))
