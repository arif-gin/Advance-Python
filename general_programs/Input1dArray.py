from numpy import *

n=int(input("Enter the number of elements:"))
a=zeros(n,dtype=int)

for i in range(n):
    x=int(input("Enter Elements:"))
    a[i]=x
print(a)
