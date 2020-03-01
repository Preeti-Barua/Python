class Mob:
    def __init__(self,m,r,s):
        self.internalmem=m
        self.Ram=r
        self.screen=s

    def displayMob(self):
            print("internal memory:",self.internalmem)
            print("RAM:",self.Ram)
            print("screen:",self.screen)

class Apple(Mob):
    def __init__(self,o):
        super().__init__('8GB','4GB',5)
        self.MacOSVersion=o
    def displayApple(self):
        print("MAc 0S version:",self.MacOSVersion)

class MI(Mob):
    def __init__(self,v,d):
        super().__init__('15GB','8GB',4)
        self.bluetoothver=v
        self.MIdrop=d

    
    def displayMI(self):
        print("bluetooth:",self.bluetoothver)
        print("mi store",self.MIdrop)

apple1=Apple('mojave')
apple1.displayMob()
apple1.displayApple()
MI1=MI(5,'abc')
MI1.displayMob()
MI1.displayMI()











        
