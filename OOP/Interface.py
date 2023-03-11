from abc import ABC,abstractmethod

class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass

class Child(Father):
    def disp1(self):
        print("Child class")
        print("Disp 1 Abstract Class")

class GrandChild(Child):
    def disp2(self):
        print("Grand Child class")
        print("Disp 2 Abstract Class")

g=GrandChild()

g.disp1()
g.disp2()
