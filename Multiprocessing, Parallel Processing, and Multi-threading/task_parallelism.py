from concurrent.futures import ProcessPoolExecutor
import numpy as np

# Define the functions
def calculate_average(array):
    return np.mean(array)

def calculate_min(array):
    return np.min(array)

def calculate_max(array):
    return np.max(array)

if __name__ == "__main__":
    array = np.random.randint(0, 100, 10000)  # array of 10,000 random integers between 0-100

    # Create a process pool executor
    with ProcessPoolExecutor() as executor:
        # Submit the tasks for execution
        average_future = executor.submit(calculate_average, array)
        min_future = executor.submit(calculate_min, array)
        max_future = executor.submit(calculate_max, array)

    print("Average:", average_future.result())
    print("Min:", min_future.result())
    print("Max:", max_future.result())
