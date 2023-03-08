# Generator

from typing import Generator


def create_generator(num: int) -> Generator:
    """Create a generator that yields numbers from 0 to num - 1."""
    for i in range(num):
        yield i


my_generator = create_generator(4)

print(my_generator)
print(list(my_generator))
