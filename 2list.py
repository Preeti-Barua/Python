list1=[]
len1=int(input("length list1:"))
for i in range( len1):
    n=int(input("enter  number of element of list1:"))
    list1.append(n)
list2=[]
len2=int(input("length l2:"))
for i in range (len2):
    n1=int(input("enter  number of element of list2:"))
    list2.append(n1)
print("list1:"+str(list1))
print("list2:"+str(list2))
if list1==list2:
    print("TRUE")
else:
    print("FALSE")
