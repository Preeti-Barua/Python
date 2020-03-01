a=int(input("enter first number."))
b=int(input("enter second number:"))
c=int(input("enter thired number:"))
if (a>b)and(a>c):
    largest=a
elif(b>a)and(b>c):
            largest=b
elif(c>a)and(c>b):
             largest=c

print("largest is:",largest)           
