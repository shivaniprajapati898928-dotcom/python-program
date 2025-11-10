# Write a Python program to create two threads- one to print even numbers and an other to print odd numbers up to n. Synchronize the threads to alternate properly. 

import threading

# Shared condition for synchronization
condition = threading.Condition()
n = int(input("Enter the limit (n): "))

# Start from 1
num = 1

def print_odd():
    global num
    while num <= n:
        with condition:
            if num % 2 == 0:
                condition.wait()
            if num <= n:
                print(f"Odd Thread: {num}")
                num += 1
                condition.notify()

def print_even():
    global num
    while num <= n:
        with condition:
            if num % 2 != 0:
                condition.wait()
            if num <= n:
                print(f"Even Thread: {num}")
                num += 1
                condition.notify()

# Create threads
t1 = threading.Thread(target=print_odd)
t2 = threading.Thread(target=print_even)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("✅ Done printing numbers alternately.")
