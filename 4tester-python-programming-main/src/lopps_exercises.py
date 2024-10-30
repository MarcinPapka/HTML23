from random import randint
from math import sqrt


def print_hello_40_times():
    for i in range(1, 41):
        print('Hello!', i)


def print_positive_numbers_divisible_by_7(start, stop):
    for i in range(start, stop + 1):
        if i % 7 == 0:
            print(i)


def print_n_random_numbers(n):
    for i in range(n):
        print(f'loop {i}:', randint(1, 1000))


# def print_square_roots_of_numbers(list_of_numbers):
#     for number in list_of_numbers:
#         print(sqrt(number))

def get_square_roots_of_numbers(list_of_numbers):
    square_roots = []
    for number in list_of_numbers:
        sqrt_of_number = round(sqrt(number), 2)
        square_roots.append(sqrt_of_number)
    return square_roots


def list_of_temperature_to_farenheit(temps_celsius):
    temps_farenheit = []
    for temp in temps_celsius:
        temps_farenheit.append(temp * 9 / 5 + 32)
    return temps_farenheit


if __name__ == '__main__':
    print_hello_40_times()
    print_positive_numbers_divisible_by_7(1, 100)
    print_n_random_numbers(20)
    print(sqrt(9))
    print((sqrt(16)))
    list_of_measurement_result = [11.0, 123, 69, 42, 23, 1, 5, 77]
    print(list_of_measurement_result)
    square_roots_of_measurements = get_square_roots_of_numbers(list_of_measurement_result)
    print(square_roots_of_measurements)

    temps_celsius = [10.3, 23.4, 15.8, 19.0, 14.0, 23.0, 25.0]
    print(list_of_temperature_to_farenheit(temps_celsius))
