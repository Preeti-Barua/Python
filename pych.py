'''
class Pycharm:
    def execute(self):
        print("compile")
        print("run")
class MyIDE:
    def execute(self):
        print("spell check")
        print("compile")
        print("run")
class Laptop:
    def code(self,ide):
        ide.execute()
py=Pycharm()
My=MyIDE()
L1=Laptop()
L1.code(My)
L1.code(py)
print("---------------------------------------------------")

class Grandparent:
    def display(self):
        print("haha")
        print("hAhA")
class Parent:
    def display(self):
        print("hehe")
        print("haha")
class children:
    def fami(self,fam):
        fam.display()

gp=Grandparent()
p=Parent()
c=children()
c.fami(gp)
c.fami(p)
print("------------------------------------------")


class Human:
    def __init__(self,n):
        self.name=n
    def disp(self):
        print("name is:",self.name)
class Doctor(Human):
    def __init__(self,sp):
        super().__init__("xyz")
        self.spec=sp
    def disp(self):
        print("name is",self.name)
        print("specialization is",self.spec)
d1=Doctor("MD")
d1.disp()
print("---------------------------------------------")
'''

class company:
    def __init__(self,cn):
        self.cname=cn
        
    def display(self):
        print("company")

class dept(company):
    def __init__(self,dn):
        super().__init__("IBM")
        self.dname=dn
        
    def display(self):
        print("Dept")

class emp(dept):
    def __init__(self,en):
        super().__init__("comp")
        self.ename=en
        
    def display(self):
        print("name is:",self.cname)
        
        print("name is:",self.dname)
    
        print("name is:",self.ename)
    
        
e=emp("pre")

e.display()












        

































































        
