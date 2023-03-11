class Father:
    def __init__(self,m):
        self.money=m
        print("Father Class Constructor")

    def show(self):
        print("Father class instance method")

class Son(Father):
    def __init__(self,m,j):
        super().__init__(m)
        self.job=j
        print("Son class constructor")

    def disp(self):
        print("Son class Instance Method:",self.money)
        print("Job:",self.job)

s=Son(1000,'Python')
s.disp()
s.show()
