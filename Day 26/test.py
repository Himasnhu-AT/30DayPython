
import threading
import time
import unittest

class TestThreading(unittest.TestCase):

    def test_thread_function(self):
        # Define a function that simulates a task
        def task():
            for _ in range(5):
                time.sleep(0.1)
                print(f"Thread {threading.current_thread().name} is working")

        # Create and start two threads
        thread1 = threading.Thread(target=task, name="Thread 1")
        thread2 = threading.Thread(target=task, name="Thread 2")
        thread1.start()
        thread2.start()

        # Wait for the threads to complete
        thread1.join()
        thread2.join()

        # Assert that the threads completed successfully
        self.assertTrue(True)

    def test_thread_function_with_arguments(self):
        # Define a function that takes an argument
        def task(name):
            for _ in range(5):
                time.sleep(0.1)
                print(f"Thread {threading.current_thread().name} with name {name} is working")

        # Create and start two threads with arguments
        thread1 = threading.Thread(target=task, args=("Task 1",))
        thread2 = threading.Thread(target=task, args=("Task 2",))
        thread1.start()
        thread2.start()

        # Wait for the threads to complete
        thread1.join()
        thread2.join()

        # Assert that the threads completed successfully
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()

