income = int(input('Income: '))
def tax(income):
    if income <= 5000:
        print(f'Należny podatek: {income*0.17}')
    else:
        higherTax = 5000*0.17 + (income-5000)*0.32
        print(f'Należny podatek: {higherTax}')
tax(income)
