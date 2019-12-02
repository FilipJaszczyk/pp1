class Statystyka():
    
    def __init__(self,zbior):
        self.zbior = zbior
    
    def __str__(self):
        return f'Zbiór: {self.zbior}'
    
    def add(self, number):
        self.zbior.append(number)
    
    def maxval(self):
        return max(self.zbior)
    
    def minval(self):
        return min(self.zbior)
    
    def srednia(self):
        return sum(self.zbior)/len(self.zbior)
    
    

arr = Statystyka([1,2,3,4,5,6])
print(arr)
arr.add(9)
print(arr)
print(f'Max:{arr.maxval()}')
print(f'Min:{arr.minval()}')
print()

