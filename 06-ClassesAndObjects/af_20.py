class Plane():
    def __init__(self,number,height=0):
        self.number = number
        self.height = 0
    def __str__(self):
        return f'Here {self.number} my height {self.height}'
    def start(self,height):
        if height > 1000 and height < 2000:
            self.height = height
        else:
            print('Warning')
    def changeHeight(self,height):
        if height > 300 and height < 11000:
            self.height = height
        else:
            print("Warning")
    def land(self):
        if self.height > 500:
            print("To high to land")
        else:
            self.height = 0
            print("Landed ")
    
plane1 = Plane('NAX4901')
print(plane1)
plane1.start(1400)
print(plane1)
plane1.changeHeight(8580)
print(plane1)
plane1.land()
plane1.changeHeight(499)
print(plane1)
plane1.land()