#collect user data
weight = float(input('Enter weight in kg '))
height = float(input('Enter height in cm '))
bmi = weight/(height/100)**2
print(f'BMI: {bmi}')