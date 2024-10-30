# Zadanie 1
def square_any_number(any_number):
    return any_number ** 2


def convert_celsius_to_fahrenheit(temp_c):
    return temp_c * 1.8 + 32


def volume_of_a_cuboid(a, b, c):
    return a * b * c


if __name__ == '__main__':
    # Zadanie 1
    print(square_any_number(0))
    print(square_any_number(16))
    print(square_any_number(2.55))

    # Zadanie 2
    print(convert_celsius_to_fahrenheit(1))

    # Zadanie 3
    print(volume_of_a_cuboid(3, 5, 7))
