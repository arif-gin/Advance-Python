lis=["Aarif",22,3.5]
marklist={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
def agkg(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)

agkg("Normal args",*lis,**marklist)
