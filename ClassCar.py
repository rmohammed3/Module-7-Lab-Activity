# Raheemuddin Mohammed
# August 27, 2025

# Problem 6: Modify the car class to include 'type' and 'manufacturer'

class car:

    def __init__(self, model, year, color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return (self.model + ' ' + str(self.year) + ' ' + self.color +
                ' ' + self.type + ' ' + self.manufacturer)

# Create objects with new attributes
car1 = car("Sports", 2012, "Blue", "Coupe", "Toyota")
car2 = car("Sedan", 2020, "Black", "Luxury", "BMW")

# Test methods
print(car1.get_color())         # Blue
print(car1.get_model())         # Sports
print(car1.get_type())          # Coupe
print(car1.get_manufacturer())  # Toyota
print(car1.fullspecs())         # Sports 2012 Blue Coupe Toyota
print(car2.fullspecs())         # Sedan 2020 Black Luxury BMW
