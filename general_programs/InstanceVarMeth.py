class Mobile:
    def __init__(self):
        self.model='Pixel'          #Instance Variable
    def show_model(self):           #Instance Method
        print(self.model)

poco=Mobile()           #Create Object
pixel=Mobile()          #Create 2nd Object

print(pixel.model)
poco.model='Poco F1'
print(poco.model)
