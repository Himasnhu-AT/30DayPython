
import threading
import time

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

print("All threads completed.")

