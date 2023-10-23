import threading
import time

import requests

max_requests = 10
semaphore = threading.Semaphore(max_requests)


def perform_get_request(url):
    try:
        response = requests.get(url)
        print(f"Done: {url}")

    except Exception as e:
        print(f"Error: {url}")
        print(str(e))
    finally:
        semaphore.release()


urls = [
    'https://www.google.com',]*50

threads = []

start_time = time.time()

for url in urls:
    thread = threading.Thread(target=perform_get_request, args=(url,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

end_time = time.time()

total_execution_time = end_time - start_time
print(f"Time is: {total_execution_time:.2f} sec")
