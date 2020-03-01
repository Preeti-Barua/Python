n=int(input("enter any number:"))
i=1
count=0
while(i<=n):
    if(n%2==0):
        count+=1
    i+=1

if(count==2):
    print("prime")
else:
    print("not")
