class Mobile:
    fp='Yes'

    def __init__(self):
        self.model='pixel'
    def show_model(self):
        print(self.model)
    @classmethod
    def is_fp(cls):
        print(cls.fp)

p=Mobile()
p.show_model()
p.is_fp()

Mobile.fp='NO'
p.is_fp()
