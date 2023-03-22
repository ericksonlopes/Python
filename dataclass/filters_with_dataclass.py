from dataclasses import dataclass
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
class CarsFilter:
    name: str = None
    year: int = None
    price: float = None
    is_used: bool = None

    def __call__(self, cars: List[Car]) -> List[Car]:
        self.cars = cars
        if self.name:
            cars = list(filter(lambda car: car.name == self.name, cars))

        if self.year:
            cars = list(filter(lambda car: car.year == self.year, cars))

        if self.price:
            cars = list(filter(lambda car: car.price == self.price, cars))

        if self.is_used:
            cars = list(filter(lambda car: car.is_used == self.is_used, cars))

        return cars

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{len(self.cars)} cars were filtered")

if __name__ == '__main__':
    chevrolet = Car('Chevrolet', 2020, 200.00, True)
    camaro = Car('Camaro', 2018, 175.52, True)
    honda = Car('Honda', 2019, 248.66, False)

    # Create list of cars
    list_car = [chevrolet, camaro, honda]

    filter_car = CarsFilter(name='Chevrolet')
    print(filter_car(list_car))
    # [Car(name='Chevrolet', year=2020, price=200.0, is_used=True)]

    filter_car = CarsFilter(year=2018)
    print(filter_car(list_car))
