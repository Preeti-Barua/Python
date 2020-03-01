n=int(input("enter the number of rows:"))
num=1
for rows in range(1,n+1):
        for col in range(1,rows+1):
            print(num,end="")
            num=num+1
        print()
