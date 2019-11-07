def recur_fibo(n):
   if n <= 1:
       return n
   else:
       #każda kolejna liczba jest sumą dwóch poprzednich zatem:
       return(recur_fibo(n-1) + recur_fibo(n-2))
ileLiczb = 20
# check number
if ileLiczb <= 0:
    print("Daj pozytywną liczbę")
elif ileLiczb == 0:
    print('')
else:
    print("Fibonacci:")
    for i in range(ileLiczb):
       print(recur_fibo(i),end=' ')
