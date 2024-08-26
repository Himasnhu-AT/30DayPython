
import unittest

class TestOOPConcepts(unittest.TestCase):

    def test_inheritance(self):
        # Create an instance of the Vehicle class
        vehicle = Vehicle("Car", 4)
        self.assertEqual(vehicle.type, "Car")
        self.assertEqual(vehicle.wheels, 4)

        # Create an instance of the Car class
        car = Car("Sedan", 4, "Automatic")
        self.assertEqual(car.type, "Sedan")
        self.assertEqual(car.wheels, 4)
        self.assertEqual(car.transmission, "Automatic")

        # Test the move() method from the Vehicle class
        self.assertEqual(vehicle.move(), "The vehicle is moving.")

        # Test the move() method from the Car class
        self.assertEqual(car.move(), "The car is moving with automatic transmission.")

    def test_polymorphism(self):
        # Create instances of the Vehicle and Car classes
        vehicle = Vehicle("Motorcycle", 2)
        car = Car("Hatchback", 4, "Manual")

        # Use the move() method for both instances
        self.assertEqual(vehicle.move(), "The vehicle is moving.")
        self.assertEqual(car.move(), "The car is moving with manual transmission.")

    def test_encapsulation(self):
        # Create an instance of the BankAccount class
        account = BankAccount(1000)

        # Access the balance through the getter method
        self.assertEqual(account.get_balance(), 1000)

        # Deposit money through the deposit method
        account.deposit(500)
        self.assertEqual(account.get_balance(), 1500)

        # Withdraw money through the withdraw method
        account.withdraw(200)
        self.assertEqual(account.get_balance(), 1300)

        # Attempt to withdraw more than the available balance
        with self.assertRaises(ValueError):
            account.withdraw(1500)

if __name__ == '__main__':
    unittest.main()

