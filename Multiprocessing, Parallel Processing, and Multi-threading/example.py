import time
import threading

# Function that sleeps for 1 second
def sleep_one_sec(i):
    print(f"Sleeping {i}...")
    time.sleep(1)
    print(f"Done {i}")

# Without threading
start = time.time()
for i in range(5):
    sleep_one_sec(i)
end = time.time()
print(f"Execution time without threading: {end - start} seconds\n")

# With threading
threads = []
start = time.time()
for i in range(5):
    thread = threading.Thread(target=sleep_one_sec, args=(i,))
    thread.start()
    threads.append(thread)

# Join all the threads to ensure they complete
for thread in threads:
    thread.join()
end = time.time()
print(f"Execution time with threading: {end - start} seconds")
