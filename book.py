class Book:
    def __init__(self, name, price_euro):
        self.name = name 
        self.price_euro = price_euro 
    
    def to_string(self):
        print(self.name + " : " + str(self.price_euro))

