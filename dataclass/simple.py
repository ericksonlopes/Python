from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    deficiency: bool
    email: str = None

    def alter_deficiency(self):
        self.deficiency = not self.deficiency

    def __str__(self):
        return f'{self.name} is {self.age} years old and has a deficiency: {self.deficiency}'


if __name__ == '__main__':
    person = Person('John', 30, False)

    # todo: add email
    print(person.email)
    # None

    # todo: Alter email
    person.email = 'python@gmail.com'
    print(person.email)

    # todo: Alter deficiency
    print(person.deficiency)
    # False

    person.alter_deficiency()
    print(person.deficiency)
    # True

    # todo: get str representation
    print(person)
    # John is 30 years old and has a deficiency: True

    # todo: get field data
    print(f'{person.name=}, {person.age=}')
    # person.name='John', person.age=30

    # todo: Person to dict
    print(person.__dict__)
    # {'name': 'John', 'age': 30}

    # todo: get Class name
    print(person.__class__.__name__)
    # Person
