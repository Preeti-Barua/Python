'''
class company:
    def __init__(self):
        self.comName=input("enter company name:")
        self.comAdd=input("enter company address:")

    def getCompanyDetails(self):
        print("company Name is:",self.comName)
        print("address is:",self.comAdd)

    def setCompanyAdd(self):
        self.comAdd=input("enter new address:")
SevenM=company()
Infi=company()

SevenM.getCompanyDetails()
Infi.getCompanyDetails()
SevenM.setCompanyAdd()
SevenM.getCompanyDetails()
Infi.getCompanyDetails()
'''
'''
class Bird:
    wings=2
    def __init__(self):
        self.name=input("enter")
b=Bird()        
print(Bird.wings)
Bird.wings=4
print(Bird.wings)
cls.wings=6

print(Bird.wings)
'''
class Book:
    pub="Naveet"

    def __init__(self):
        self.name=input("enter the name :")
        
        self.price=input("enter the price :")
        self.edi=input("enter the edition :")


    def getBookDetails(self):
        print("enter the publication:",self.pub)
        print("enter the name:",self.name)
        print("enter the price:",self.price)
        print("enter the edition:",self.edi)

    def setprice(self):
        self.price=5000
    @classmethod
    def ModifyPub(cls):
        cls.pub="MC hill"

a=Book()

a.getBookDetails()

a.setprice()
a.ModifyPub()
a.getBookDetails()


















    












