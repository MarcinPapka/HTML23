import random
import time


def generate_random_email():
    domain = 'example.com'
    name_list = ['kasia', 'basia', 'gosia', 'zosia']
    random_name = random.choice(name_list)
    # suffix = random.randint(1, 1_000_000)
    suffix = time.time()
    return f'{random_name}.{suffix}@{domain}'


def generate_seniority_years():
    return random.randint(0, 40)


def generate_random_boolean():
    return random.choice([True, False])


def get_dictionary_with_random_personal_data():
    random_email = generate_random_email()
    random_number = generate_seniority_years()
    random_boolean = generate_random_boolean()
    return {
        "email": random_email,
        "seniority_years": random_number,
        "female": random_boolean
    }


def generate_list_of_dictionaries_with_random_personal_data(number_of_dictionaries):
    list_of_dictionaries = []
    for number in range(number_of_dictionaries):
        list_of_dictionaries.append(get_dictionary_with_random_personal_data())
    return list_of_dictionaries


if __name__ == '__main__':
    print(get_dictionary_with_random_personal_data())
    print(generate_list_of_dictionaries_with_random_personal_data(2))
