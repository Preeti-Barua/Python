##l=[1,2,3,4,5]
##l_sq=[i*i*i for i in l]
##print(l_sq)

##l=[1,2,7,12,15,20,5]
##l_even=[i**3 for i in l if i%2==0]
##print(l_even)    

       
l=[]
len=int(input("enter the total numbers you want:"))
for i in range(len):
    n=int(input("enter numbers:"))
    l.append(n)
l_odd=[i**3 for i in l if i%2==1]
print(l_odd)    
