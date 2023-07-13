import grequests
import time
import threading

def send_grequests(url_list):
    

    # Create a list of request objects using grequests
    requests = (grequests.get(url, timeout=5) for url in url_list)

    # Send the requests asynchronously
    responses = grequests.map(requests)

    

    print('Thread Executed!')

   
  


if __name__ == "__main__":

    start_time = time.time()
    # Open the file containing URLs
    with open('urls.txt', 'r') as file:
        url_list = [line.strip() for line in file]

    threads = []
    batch_size = 100

    # Divide the URL list into batches
    for i in range(0, len(url_list), batch_size):
        url_batch = url_list[i:i+batch_size]
        thread = threading.Thread(target=send_grequests, args=(url_batch,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end_time = time.time()
    execution_time = end_time - start_time

    print("Script execution time:", execution_time, "seconds")





    