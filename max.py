list=[]
ge=int(input("enter the total numbers:"))
for i in range(ge):
    a=int(input("enter the numbers:"))
    list.append(a)
    max=list[0]
    for a in list:
        if a>max:
            max=a
print("maxi:",max)
