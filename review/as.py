# Object Oriented Programming
# OOP
# برنامه نویسی شی‌گرا

class Car:
    count = 0
    company = ''
    model = ''
    tyre = 4
    color = ''
    max_speed = 100
    fuel = 10
    
    # dunder init
    def __init__(self):
        print('TaDaaaaaaa!')
        Car.count += 1
    
    # function , method
    def tada(self):
        print('My car is a', self.model, 'and It use',
              self.fuel, 'for 100 KMs.')
    
    
p = Car()  # instance نمونه     object شی
# p.company = 'Peugeot'
# p.model = '207i'
# p.color = 'violet'
# p.max_speed = 320

# print(p.fuel)

# p.tada()