from dataclasses import dataclass
from functools import reduce
from typing import List


@dataclass
class Car:
    name: str
    year: int
    price: float
    is_used: bool

    def __str__(self):
        return f'{self.name} was made in {self.year} and costs {self.price}'


@dataclass
class Cars:
    list_cars: List[Car]

    def filter_used(self) -> List[Car]:
        return list(filter(lambda car: car.is_used, self.list_cars))

    def disable_all_used(self) -> List[Car]:
        return list(map(lambda car: Car(car.name, car.year, car.price, False) if car.is_used else car, self.list_cars))

    def all_price(self) -> float:
        return reduce(lambda x, y: x + y.price, self.list_cars, 0)


if __name__ == '__main__':
    chevrolet = Car('Chevrolet', 2020, 200.00, True)
    camaro = Car('Camaro', 2018, 175.52, True)
    honda = Car('Honda', 2019, 248.66, False)

    print(chevrolet)
    # Chevrolet was made in 2020 and costs 200.0

    # todo: create list of cars
    list_car = [chevrolet, camaro, honda]

    # todo: create Cars
    cars = Cars(list_car)
    print(cars.list_cars)
    # [Car(name='Chevrolet', year=2020, price=200.0, is_used=True),
    # Car(name='Camaro', year=2018, price=175.52, is_used=True),
    # Car(name='Honda', year=2019, price=248.66, is_used=False)]

    # todo: filter used cars
    cars_activate = cars.filter_used()
    print(cars_activate)
    # [Car(name='Chevrolet', year=2020, price=200.0, is_used=True),
    # Car(name='Camaro', year=2018, price=175.52, is_used=True)]

    # todo: deactive all used cars
    cars.list_cars = cars.disable_all_used()
    print(cars.list_cars)
    # [Car(name='Chevrolet', year=2020, price=200.0, is_used=False),
    # Car(name='Camaro', year=2018, price=175.52, is_used=False),
    # Car(name='Honda', year=2019, price=248.66, is_used=False)]

    # todo: get all price
    preco = cars.all_price()
    print(preco)
    # 624.18
