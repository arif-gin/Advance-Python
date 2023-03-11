from array import *

#For loop
stu=array('i',[1,2,3,4,])
l=len(stu)
for i in range(l):
    print(stu[i])
print(" \n")
#while loop
j=0
while j<l:
    print(stu[j])
    j+=1

#append
print("Array after append")
stu.append(5)
print(stu)
print(l)
