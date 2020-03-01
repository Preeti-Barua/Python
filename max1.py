l=[]
len=int(input("enter the length:"))
for i in range(len):
    n=int(input("enter the elements:"))
    l.append(n)
    max=l[0]
for n in l:
    if n>max:
        max=n
print("maximum is:",max)       
##l.remove(max)
##print(l)
##for n in l:
##        n>max
##        max=n
##print("second maxi is:",max)        
l.sort()
print(l)
print("second largest is:",l[-2])
