a=float(input("enter 1st marks:"))
b=float(input("enter 2nd marks:"))
c=float(input("enter 3rd marks:"))
d=float(input("enter 4th marks:"))
e=float(input("enter 5th marks:"))
sum=a+b+c+d+e

per=(sum/500)*100
print("percentage= ",per)
if(per>=75):
    grade="Aplus"
elif(per<75)and(per>=60):
    grade="A"
elif(per<60)and(per>=45):
    grade="B"
elif(per<45)and(per>=35):
    grade="C"
elif(per<35):
    grade="FAIL"    
    
print("your grade is:",grade)
