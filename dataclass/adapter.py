from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


def from_person(data: dict):
    return Person(**data)


if __name__ == '__main__':
    person_dict = {'name': 'John', 'age': 30}

    print(from_person(person_dict))
    # Person(name='John', age=30)
