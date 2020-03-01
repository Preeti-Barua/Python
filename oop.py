##class demo:
##    def disp(self):
##        print("hello")
##obj1=demo()
##obj1.disp()
##class Stud:
##    def __init__(self):
##        print("hello")
##
##s1=Stud()

class stud:
    def __init__(self,r,n,age):
        self.rollno=r
        self.name=n
        self.age=age

    def dis(self):
        print("roll is:",self.rollno)
        print("name is:",self.name)
        print("age:",self.age)
a=stud(101,'ABC',3)
b=stud(102,'XYZ',34)
b.dis()
a.dis()
       
