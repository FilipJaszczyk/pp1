limit = int(input('Podaj limit prędkości: '))
velocity = int(input('Podaj prędkość pojazdu: '))
diff = velocity - limit
counter = -10
if diff <= 0:
    print('Bez mandatu')
elif diff > 0 and diff <= 10:
    print(f'Mandat: {diff*5}')
elif diff > 10:
    for i in range(diff):
        counter += 1
    print(f'Mandat: {50+counter*15}')
        
        
    