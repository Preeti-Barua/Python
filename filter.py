##
##li=list(filter(lambda x:x%2==0,range(1,21)))
##print (li)


    
    
        
##list=list(filter(lambda x:x%5==0 and x%7==0,range(1,100)))
##print (list)
##
##add=lambda x,y,z:x+y+z
##a=add(2,3,4)
##print("sum is:",a)
##print(a)
##
##l=[]
##len=int(input("enter the length:"))
##for i in range(len):
##    l.append(i)
##fz=frozenset(l)
##list1=list(filter(lambda x:x%5==0 and x%7==0,fz))
##print(list1)
from functools import* 
##l=[1,3,4,7,18]
##res=reduce(lambda a,b:a+b,l)
##print("sum is:",res)


a=reduce(lambda c,b:c*b, range(20,36))
print(a)
