class Student:
    def __init__(self,n,r):
        self.name=n
        self.roll=r

    def disp(self):
        print("Student Name:",self.name)
        print("Student Roll:",self.roll)

class User:
    @staticmethod
    def show(s):
        print("User Name:",s.name)
        print("User Roll:",s.roll)
        s.disp()

stu=Student('Aarif',101)
User.show(stu)
