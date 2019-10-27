x = int(input('Podaj kwotę w zł: '))
r5 = x // 5
r2 = (x % 5) // 2
r1 = (x - r5*5 - r2*2) // 1
print(f'5 zł - {r5}\n2 zł - {r2}\n1 zł - {r1}')