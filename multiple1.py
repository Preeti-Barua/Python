class Pet:
    def __init__(self,n):
        super().__init__("yellow")
        self.name=n
    def displayPet(self):
        print("name of the pet is:",self.name)
class Wild:
    def __init__(self,c):
        self.color=c
    def displaywild(self):
        print("color is:",self.color)
class Animal(Pet,Wild):
    def __init__(self,t):
        super().__init__("Tiger")
        self.types=t
    def displayanimal(self):
        print("animal type:",self.types)
a=Animal('Wild')
a.displayPet()
a.displaywild()
a.displayanimal()
print("-------------------------------------------------")
class car:
    def __init__(self):
        self.color="blue"
        self.mileage=50
    def displaycar(self):
        print("color of the car is:",self.color)
        print("mileage of the car is:",self.mileage)
class BMW(car):
    def __init__(self):
        super().__init__()
        self.logo="logo"
    def displayBMW(self):
        print("logo is:",self.logo)
class Mseries(BMW):
    def __init__(self):
        super().__init__()
        self.airbags="a"
        self.power=123
        self.enginetype="en"
        
    def displayMseries(self):
        print("airbag",self.airbags)
        print("power",self.power)
        print("enginetype",self.enginetype)
a=Mseries()
a.displaycar()
a.displayBMW
a.displayMseries()














        
      
