dict={}
len=int(input("enter the length:"))
for i in range(len):
    k=int(input("enter the key :"))
    v=int(input("enter the value:"))
    
    dict[k]=v
sum=0
for i in dict:
    sum=sum+v
print("sum of keys:",sum)



##print(sum1)

