a=int(input("enter a number""))
sum=0
temp=a
while(a>0):
    r=a%10
    sum=sum*10+r
    a=a//10
a=temp
if(a==sum):
     print("its palindrome")
else:
     print("no")
 
