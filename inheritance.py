##***
##class Base:
##    def methodBase(self):
##        print("In base class")
##class child(Base):
##    def methodchild(Base):
##        print("In child class")
##c1=child()
##c1.methodBase()
##c1.methodchild()
##***


##class Base:
##    def ___init__(self):
##        print('base')
##class child(Base):
##    pass
##
##
##c1=Base()


class stud:
    def __init__(self,r,n):
        self.rollno=r
        self.name=n
    def Displaystud(self):
        print("enter rollno :",self.rollno)
        print("name is :",self.name)
class ArtsStud(stud):
    def __init__(self,t):
        super().__init__(101,'abc')
        self.typeOfArt=t

    def DisplayArtsStud(self):
        print("enter the type of art:",self.typeOfArt)

s1=ArtsStud("dance")
s1.Displaystud()
s1.DisplayArtsStud()



class Animal():
    def __init__(self,n,c,a):
        self.name=n
        self.color=c
        self.age=a
    def DisplayA(self):
        print("nameof the animal:",self.name)
        print("color:",self.color)
        print("age:",self.age)

class breed(Animal):
    def __init__(self,t):
        super().__init__("dog","black","4yrs")
        self.breedname=t
    def DisplayB(self):
        print("breed is:",self.breedname)
c1=breed("doberman")
c1.DisplayA()
c1.DisplayB()

        



        





















    
