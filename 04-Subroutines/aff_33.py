tab =[]
def fib(n):
    if n == 0:
        print('')
    else:
        tab.append(0)
        a, b = 0, 1
            #?
        for i in range(n-1):
            a, b = b,a+b
            tab.append(a)
    return tab
print(fib(1))
