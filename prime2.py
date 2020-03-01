##n=int(input("enter a number:"))
##i=1
##
##count=0
##while(i<n):
##    if(n%i==0):
##        count=count+1
##
##    i=i+1        
##if(count<=2):
##    print("prime")
##else:
##    print("not")


i=2
j=2

while(i<=10):
    while(j<i):
        if(i%j==0):
            break;
        else:   
            print(i)
        j+=1
    i+=1      
