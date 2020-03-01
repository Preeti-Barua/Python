class car:
    def __init__(self,p,m,c):
        self.price=p
        self.model=m
        self.color=c
    def displaycarDetails(self):
        print("price is:",self.price)
        print("model is:",self.model)
        print("color is",self.color)
    def Modify(self,p):
        self.price=p

c1=car("10lac","honda city","white")
c2=car("1cr","jaguar","black")
c1.Modify("8lac")
c1.displaycarDetails()
c2.displaycarDetails()
print("--------------------------------------")
class college:
    city="pune"
    code=2344
    def __init__(self,b,c,r):
        self.branch=b
        self.college=c
        self.rank=r
    def displayDetails(self):
        print("branch:",self.branch)
        print("college:",self.college)
        print("rank is",self.rank)
        print("city is:",self.city)
        print("code is:",self.code)
    @classmethod
    def Modifycity(cls):
        cls.city="mumbai"
        cls.code=123

c1=college("fc road ","FC","3")
c2=college("kothrud","MIT","1")
c1.Modifycity()

c1.displayDetails()
c2.displayDetails()
print("-----------------------------------------------------------------------------")


class Bird:
    wings=2
    def __init__(self,n,b,c):
        self.name=n
        self.breed=b
        self.color=c

    def display(self):
        print("name is:",self.name)
        print("breed is:",self.breed)
        print("color is:",self.color)
        print("wings are:",self.wings)

    def Modifycolor(self,c):
        self.color=c

        
b1=Bird("parrot","ddsfs","green")
b2=Bird("sparrow","agaaag","brown")
b1.Modifycolor("blue")
b1.display()
b2.display()
        































