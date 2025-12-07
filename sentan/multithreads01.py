import threading

# Shared variable
counter = 0

# Lock to prevent race conditions
lock = threading.Lock()

def increment():
    global counter
    with lock:
        counter += 1
        print(f"Counter incremented to {counter}")

# Create two threads
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print(f"Final counter value: {counter}")
