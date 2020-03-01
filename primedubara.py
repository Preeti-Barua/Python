n=int(input("enter a number:"))
i=2
while(i<=n):
    c=0
    j=2
    while(j<i):
        if(i%j==0):
            c+=1
        j+=1
     
    if(c==0):
        print(i)
    i=i+1
