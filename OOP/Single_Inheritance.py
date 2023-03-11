class Father:
    money=1000000

    @classmethod
    def showmoney(cls):
        print("Parent Class Method:",cls.money)

    @staticmethod
    def stat():
        a=10
        print("Parent class static method:",a)

class Son(Father):
    def disp(self):
        print("Child class instance method")

s=Son()
s.disp()
s.showmoney()
s.stat()
