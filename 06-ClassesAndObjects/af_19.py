class account():
    def __init__(self,number):
        self.number = number
        self.saldo = 0
    def __str__(self):
        return f'Number: {self.number}\nSaldo: {self.saldo} ' 
    def cash_in(self,cashIn):
        self.saldo += cashIn
        return self.saldo
    def cash_out(self,cashOut):
        self.saldo -= cashOut
        return self.saldo
    
acc = account('11 1111 1111 1111 1111 1111 1111')
print(acc)
acc.cash_in(40)
print(acc)
acc.cash_out(20)
print(acc)