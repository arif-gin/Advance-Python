class Army:
    def __init__(self):
        self.name='Aarif'
        self.age=23
        self.nationality='Bangladeshi'
        self.gn=self.Gun()

    def show(self):
        print("Name:",self.name)
        print("Age:", self.age)
        print("Nationality:", self.nationality)

    class Gun:
        def __init__(self):
            self.name='AK47'
            self.capacity='75 rounds'
            self.length='34.3 IN'

        def disp(self):
            print("Gun Name:",self.name)
            print("Gun Capacity:", self.capacity)
            print("Gun Length:", self.length)

a=Army()
g=Army().Gun()
a.show()

print()

g.disp()
# a.gn.disp()
