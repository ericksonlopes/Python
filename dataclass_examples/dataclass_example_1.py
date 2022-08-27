from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


if __name__ == '__main__':
    # todo: create person
    person = Person(name='John', age=30)
    print(person)
    # Person(name='John', age=30)

    # todo: get field data
    print(f'{person.name=}, {person.age=}')
    # person.name='John', person.age=30

    # todo: Person to dict
    print(person.__dict__)
    # {'name': 'John', 'age': 30}

    # todo: get Class name
    print(person.__class__.__name__)
    # Person
