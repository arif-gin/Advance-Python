l=[1,2,4]
l2=[]

def square(num):
    return num*num

for item in l:
    l2.append(square(item))

print(l2)

#method 2 map

print(list(map(square,l)))
