import concurrent.futures
import json
from typing import Generator

import requests

url = "https://jsonplaceholder.typicode.com/todos/"


def make_request(id_user: str) -> bytes:
    """Faça uma solicitação para a url e retorne o conteúdo da resposta"""
    response = requests.get(url + id_user)
    return response.content


def main() -> Generator[dict, None]:
    """Use concurrent.futures para fazer várias requisições de uma só vez"""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        tasks = [executor.submit(make_request, id_user=str(num)) for num in range(10)]

        for result in concurrent.futures.as_completed(tasks):
            yield json.loads(result.result())


lista_requests = list(main())
print(lista_requests)
