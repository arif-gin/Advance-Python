marklist={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
def pm(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)

pm(**marklist)
