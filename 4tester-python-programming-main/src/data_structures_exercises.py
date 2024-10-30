def calculate_average_of_list_numbers(input_list):
    return sum(input_list) / len(input_list)


def calculate_average_of_two_numbers(a, b):
    return (a + b) / 2


if __name__ == '__main__':
    january = [-4, 1.0, -7, 2]
    february = [-13, -9, -3, 3]
    january_average = calculate_average_of_list_numbers(january)
    february_average = calculate_average_of_list_numbers(february)
    bimonthly_average = calculate_average_of_two_numbers(january_average, february_average)
    print(bimonthly_average)

# Zadanie 2


import string
import random


# Get random password pf length 8 with letters, digits, and symbols
def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(8))


# Function generating random login data
def generate_login_data(email_address):
    generated_password = generate_random_password()
    return {"email": email_address, "password": generated_password}


if __name__ == '__main__':
    print(generate_login_data("andor@starwars.com"))
    print(generate_login_data("mando@starwars.com"))
    print(generate_login_data("kenobi@starwars.com"))
