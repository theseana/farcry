class Car:

    def __init__(self, com, mod, ty, col, max_s):
        self.company = com
        self.model = mod
        self.tyre = ty
        self.color = col
        self.max_speed = max_s
    
        
a = Car('IranKhodro', 'PayKan', 4, 'White', 400)

print(a.company)