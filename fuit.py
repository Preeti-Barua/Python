class Fruit:
    fruit_type="Orange"
    def __init__(self):
        self.name=input("enter the name:")
        self.season=input("enter the season:")
        self.price=input("enter the price:")
    def getDetails(self):
        print("enter the name:",self.name)
        print("enter the season:",self.season)
        print("enter the price:",self.price)
        print("enter the fruit type:",self.fruit_type)
    def setModify(self):
        self.season="autumn"
        self.price=122345
    @classmethod
    def modifyfruit_type(cls):
        cls.fruit_type="apple"
a=Fruit()
a.getDetails()
a.setModify()
a.modifyfruit_type()
a.getDetails()
        
