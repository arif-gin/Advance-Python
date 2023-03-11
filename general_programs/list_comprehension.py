list1=[3,6,7,8,9,2,4,23,75,89,123,66]
# b=[]
#
# for item in list1:
#     if item%2==0:
#         b.append(item)
#
# print(b)


#shortcut
b=[i for i in list1 if i%2==0]
print(b)

#set comprehension

t=[1,4,2,4,1,2,3]
s={i for i in t}
print(s)
