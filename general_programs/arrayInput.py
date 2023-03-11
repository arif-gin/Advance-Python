from array import *

stu=array('i',[])
n=int(input("Enter the number of elements:"))

for i in range(n):
    stu.append(int(input("Enter the elements:")))

for i in range(n):
    print(stu[i])
