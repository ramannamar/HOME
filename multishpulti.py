from multiprocessing import Process
import time
import requests


def perform_get_request(url):
    try:
        response = requests.get(url)
        print(f"Done: {url}")
    except Exception as e:
        print(f"Error: {url}")
        print(str(e))


if __name__ == "__main__":
    urls = ['https://www.google.com']*100

    start_time = time.time()

    processes = []

    for url in urls:
        process = Process(target=perform_get_request, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()

    total_execution_time = end_time - start_time
    print(f"Time is: {total_execution_time:.2f} sec")
