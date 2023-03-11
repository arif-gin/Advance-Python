
def decor(fun):
    def inner():
        print("IF: Before enhancing function")
        fun()
        print("IF: After enhancing function")
    return inner

def num():
    print("we will use this function")

result=decor(num)
result()
