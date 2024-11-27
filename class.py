# Parent class
class SmartPhone:
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model

    # Creating a method for the parent class
    def display_info(self):
        return f'This is a {self.color} sleek {self.brand} {self.model} phone.'


# Creating an object of the parent class
mobile = SmartPhone('black', 'Apple', 'iPhone 13')
print(mobile.display_info())  # Output: This is a black sleek Apple iPhone 13 phone.


# Child class inheriting from SmartPhone
class iPhone(SmartPhone):
    def __init__(self, color, brand, model):
        super().__init__(color, brand, model)
        self.cover = 'glass'

    # Overriding the display_info method
    def display_info(self):
        return f'This is a {self.color} good {self.brand} {self.model} with a {self.cover} cover.'


# Creating an object of the child class
iphone1 = iPhone('white', 'Apple', 'iPhone 14')
print(iphone1.display_info())  # Output: This is a white good Apple iPhone 14 with a glass cover.
