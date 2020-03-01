l=[1,2,3,['hello',10],20.15]
for i in l:
    if type(i)==list:
        for j in i:
            print(j,end=" ")

    else:
        print(i,end="  ")
        
