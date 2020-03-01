n=int(input("enter a number:"))
sum=0
temp=0
temp=n
while(n>0):
    r=n%10
    sum=sum+r**3
    
    
    n=n//10

if(temp==sum):
    print("its armstrong.")
else:
    print("no")
