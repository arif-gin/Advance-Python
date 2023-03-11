#reduce applies a rolling computation to sequential pair of elements
from functools import reduce

sum=lambda a,b:a+b

l=[1,2,3,4]
val=reduce(sum,l) #l in sum then 1+2=3+3=6+4=10
print(val)
