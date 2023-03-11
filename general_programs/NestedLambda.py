add=lambda  x=10 : (lambda y:x+y)
a=add()
print(a(10))


#Returning Lambda Function from a Function in Python
def plus():
    c=90
    return (lambda b:b+c )
p=plus()
print(p(10))
