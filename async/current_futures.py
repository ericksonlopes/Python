import requests
import concurrent.futures

url = "https://jsonplaceholder.typicode.com/todos/3"


def make_request():
    """Make a request to the url and return the response content"""
    response = requests.get(url)
    return response.content

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(make_request) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
