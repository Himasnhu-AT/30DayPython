
# Day 10 code implementation in Python

class Car:
    """Represents a car with color and number of wheels."""

    def __init__(self, color, wheels):
        """Initializes a new Car object."""
        self.color = color
        self.wheels = wheels

    def honk(self):
        """Simulates the car honking."""
        return "Beep! Beep!"

# Create an instance of the Car class
my_car = Car("Blue", 4)

# Access the attributes of the object
print(f"My car is {my_car.color} and has {my_car.wheels} wheels.")

# Call the honk method
print(my_car.honk())

