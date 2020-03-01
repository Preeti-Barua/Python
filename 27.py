'''
class stud:
    def __init__(self,m):
        self.marks=m
    def __add__(self,other):
        s=self.marks+other.marks
        res=stud(s)
        return res
s1=stud(70)
s2=stud(80)
s3=s1+s2
print(s3.marks)
'''
'''
class stud:
    def __init__(self,m):
        self.marks=m
    def __mul__(self,other):
        s=self.marks*other.marks
        res=stud(s)
        return res
    
s1=stud(70)
s2=stud(80)
s3=s1*s2
print(s3.marks)
'''
class stud:
    def __init__(self,m):
        self.marks=m
    def __floordiv__(self,other):
        s=self.marks//other.marks
        res=stud(s)
        return res
s1=stud(8)
s2=stud(2)

s4=s1//s2
print(s4.marks)
