class veggi:
    veg="onion"
    def __init__(self):
        self.name=input("enter the name:")
        self.price=input("enter the price:")
        self.color=input("enter the color:")
        self.season=input("enter the season :")
        self.veg=input("enter the type:")

    def getDisplay(self):
        print("enter the name:",self.name)
        print("enter the price",self.price)
        print("enter the color",self.color)
        print("enter the season",self.season)
    def setchange(self):
        self.color="blue"
        self.price="200"
    @classmethod
    def Modifyveg(cls):
        cls.Modify="potato"
a=veggi()

a.getDisplay()
a.setchange()
a.Modifyveg()
a.getDisplay()
