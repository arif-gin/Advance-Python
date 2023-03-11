from abc import  ABC,abstractmethod

class DefenceForce(ABC):
    def __init__(self):
        self.id=101
    @abstractmethod
    def area(self):
        pass
    def gun(self):
        print("Gun = AK47","ID:",self.id,"\n")
class Army(DefenceForce):
    def area(self):
        print("Army Area = Land")

class AirForce(DefenceForce):
    def area(self):
        print("AirForce Area = Sky")

class Navy(DefenceForce):
    def area(self):
        print("Navy Area = Ocean")

af= AirForce()
a=Army()
n=Navy()

af.area()
af.gun()

a.area()
a.gun()

n.area()
n.gun()
