list=[]
length=int(input("enter length:"))
for i in range(length):
    n=int(input("enter elements:"))
    list.append(n)
    
print("list:"+str(list))
min=list[0]
for n in list:
    if n<min:
        min=n
print("min:",min)        
