# Write a multithreaded program where multiple threads update a shared counter variable. Use Lock to prevent race conditions. 

import threading
import time

# Shared counter variable
counter = 0

# Create a Lock object
lock = threading.Lock()

# Function for each thread to increment the counter
def update_counter(thread_name, increments):
    global counter
    for _ in range(increments):
        # Acquire the lock before modifying the shared variable
        with lock:
            temp = counter
            temp += 1
            counter = temp
        # Optional: small delay to simulate work
        time.sleep(0.001)
    print(f"{thread_name} finished updating counter.")

# Number of threads and increments per thread
num_threads = 5
increments_per_thread = 100

# Create threads
threads = []
for i in range(num_threads):
    t = threading.Thread(target=update_counter, args=(f"Thread-{i+1}", increments_per_thread))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print(f"\n Final Counter Value: {counter}")
print(f"Expected Value: {num_threads * increments_per_thread}")
