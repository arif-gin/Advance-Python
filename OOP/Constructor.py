class Mobile:
    def __init__(self):
        self.model='Poco F1'
        self.camera='10px'
        self.ram='8gb'

    def show_model(self):
        print('Model:',self.model)
        print('Camera:',self.camera)
        print('Ram:',self.ram)

    def price(self,price):
        print('Price of',self.model,':',price)

m=Mobile()
m.show_model()
m.price(10)
