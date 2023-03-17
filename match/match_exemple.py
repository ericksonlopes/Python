data = ["erick", "santos", "silva"]

match data:
    case []:
        print('Empty')
    case [first, second, ]:
        print(f"{first} and {second}")
    case [first, second, third]:
        print(f"{first} and {second} and {third}")

    case _:
        raise ValueError('Invalid data')


def calculator(a, b, operator):
    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case _:
            raise ValueError('Invalid operator')


print(calculator(1, 2, '+'))
