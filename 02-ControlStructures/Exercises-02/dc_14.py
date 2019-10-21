dog_age = int(input('enter dog age'))
if dog_age == 1:
    print('10.5')
elif dog_age == 2:
    print('21')
elif dog_age > 2:
    dog_age =  21 + (dog_age-2)*4
    print(f'{dog_age}')