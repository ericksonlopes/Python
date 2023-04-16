from dataclasses import dataclass


@dataclass
class Car:
    name: str
    year: int
    price: float
    is_used: bool


car_var = Car('Chevrolet', 2020, 200.00, True)

if isinstance(car_var, Car):
    print('car_var is a Car')
