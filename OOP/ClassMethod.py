class Mobile:
    fp='yes'
    @classmethod
    def show_model(cls,ram):
        # cls.ram=r
        print("Fingerprint:",cls.fp)
        print('RAM:',ram)

realme=Mobile()
realme.show_model('4GB')


class Name:
    first_name="Aarif"
    @classmethod
    def show_name(cls,last_name):
        print("Full Name:",cls.first_name,"",last_name)

n=Name()
n.show_name("Hussain")
