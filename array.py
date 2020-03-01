from array import *
##arr=array('i',[])
##l=int(input("enter the length of array:"))
##for i in range(l) :
##    num=int(input("enter the elements:"))
##    arr.append(num)
##print("array is:",arr)

arr=array('i',[1,2,3,4])
arr1=array('d',[1.1,4.2,4.0,5.2])
res=array('d',[])
res=arr+arr1
print("array is",res)          


           
arr=array('i',[1,2,3,4,6,7,5])
count=0
count1=0
for j in arr:
    if j%2==0:
        count+=1
    else:
         count1+=1
        
print("even is",count)
print("odd is",count1)

            
