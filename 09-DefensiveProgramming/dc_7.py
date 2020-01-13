wzrost = int(input("Podaj wzrost "))
waga = float(input("Podaj wagę "))

assert type(wzrost) == int and wzrost > 150 and wzrost <220, "Type or range error"
assert type(waga) == float and waga > 40 and waga <150, "Type or range error"

def BMI(wzrost,waga):
    bmi = waga/(wzrost/100)**2
    return bmi
print(BMI(wzrost,waga))