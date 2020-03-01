class living:
    def __init__(self,n,res):
        self.name=n
        self.res=res
    def displayliv(self):
        print("name:",self.name)
        print("growth:",self.res)
class plant(living):
    ##super().__init__("flowerplant","carbondioxide")
    def __init__(self,mv,sou):
        super().__init__("flowerplant","carbondioxide") 
        self.movement=mv
        self.sound=sou
    def displayPlant(self):
        print("self movement:",self.movement)
        print("sound:",self.sound)
    

class animal(living):
       def __init__(self,typ,sen):
           super().__init__("lion","oxy")
           self.foodtype=typ
           self.sensory=sen

       def displayanimal(self):
            print("food type:",self.foodtype)
            print("sensory:",self.sensory)

a=plant('yes','y')
a.displayliv()
a.displayPlant()
b=animal('hetro','yas')
b.displayliv()
b.displayanimal()







            
