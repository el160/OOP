class Vehicle :
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        
        #creating method for the class
    def move(self):
        return f'This as a {self.color} {self.model} {self.year} Vehicle'

class Plane:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        
    def move(self):
        return f'A {self.color} huge {self.model} {self.year} plane has landed'
        
        
class Bike(Vehicle) :
    def __init__(self, color, model, year):
        super().__init__(color, model, year)
        self.gears =6
    def move(self):
        return f'This is a {self.color} {self.model} bike made in {self.year}'
#adding a new method to the class Bike
    def shifts(self):
        return f'The bike has {self.gears} gears'
    
#creating objects for the classes
car = Vehicle('red', 'Toyota', 2015)
jet = Plane('blue', 'Boeing', 2017)
cycle = Bike('green', 'Suzuki', 2022)

for y in [car, jet, cycle]:
 print (y.move())
    
