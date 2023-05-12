class Book:
    first_price = 0 
    last_price = 0 

    def __init__(self, name, price_euro):
        self.name = name 
        self.price_euro = price_euro 
    
    def to_string(self):
        print(self.name + " : " + str(self.price_euro))

    def get_price_variation(self):
        return self.last_price - self.first_price


