
"""
Day 11: OOP - Inheritance, Polymorphism, and Encapsulation

Complete the following code to demonstrate the concepts of inheritance, polymorphism, and encapsulation.

LICENSE: ALL RIGHTS RESERVED (C) 2024 @OpenEdu <git: openeduhq> @Himanshu <git: himanshu-at>

"""


class Vehicle:
    """Represents a generic vehicle."""

    def __init__(self, type, wheels):
        self.type = type
        self.wheels = wheels

    def move(self):
        """Method to simulate the vehicle moving."""
        return "The vehicle is moving."


class Car(Vehicle):
    """Represents a car, inheriting from Vehicle."""

    def __init__(self, type, wheels, transmission):
        # Initialize the parent class's attributes using super()
        # ...

        self.transmission = transmission

    def move(self):
        """Method to simulate the car moving, overriding the Vehicle's move method."""
        return f"The car is moving with {self.transmission} transmission."


class BankAccount:
    """Represents a bank account."""

    def __init__(self, balance):
        # Encapsulate the balance using double underscores (__)
        # ...

    def get_balance(self):
        """Getter method to access the balance."""
        # ...

    def deposit(self, amount):
        """Method to deposit money into the account."""
        # ...

    def withdraw(self, amount):
        """Method to withdraw money from the account."""
        # ...

# Create instances of Vehicle and Car to test inheritance and polymorphism
# ...

# Create an instance of BankAccount to test encapsulation
# ...
