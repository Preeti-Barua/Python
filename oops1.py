class employee:
    def __init__(self,id,name,sal):
        self.eid=id
        self.ename=name
        self.esal=sal

    def dispEmpDetails(self):
        print("emp id",self.eid)
        print("emp name",self.ename)
        print("emp esalary",self.esal)
e1=employee(101,"qwerty",1120)
e1.dispEmpDetails()
    
