
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
        # Initialize the parent class's attributes
        super().__init__(type, wheels)
        self.transmission = transmission

    def move(self):
        """Method to simulate the car moving, overriding the Vehicle's move method."""
        return f"The car is moving with {self.transmission} transmission."


class BankAccount:
    """Represents a bank account."""

    def __init__(self, balance):
        self.__balance = balance  # Use double underscores to make balance private

    def get_balance(self):
        """Getter method to access the balance."""
        return self.__balance

    def deposit(self, amount):
        """Method to deposit money into the account."""
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Method to withdraw money from the account."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient funds or invalid withdrawal amount.")

