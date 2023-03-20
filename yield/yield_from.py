# Generator

from typing import Generator


def create_generator(num: int) -> Generator:
    """Create a generator that yields numbers from 0 to num - 1."""
    return_list = []
    for i in range(num):
        return_list.append(i)
        
    yield from return_list


my_generator = create_generator(4)

print(my_generator)
print(list(my_generator))
