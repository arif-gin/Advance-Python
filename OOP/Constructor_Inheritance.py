class Father:
    def __init__(self):
        self.money=1000
        print("Father Class Constructor","\n")

    def show(self):
        print("Father Class Instance Method","\n")

class Son(Father):
    def disp(self):
        print("Son Class Instance Method","\n")
        print("Father Inheritance Money:",self.money)

s=Son()
print(s.money)
s.show()
s.disp()
