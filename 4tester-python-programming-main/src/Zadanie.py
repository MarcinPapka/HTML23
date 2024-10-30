import random
from dateutil.utils import today

list_of_women_names = ["Sophia", "Emily", "Mary", "Susan", "Lily"]
list_of_man_names = ["Jake", "Jack", "Harry", "Jacob", "James"]
list_of_last_names = ["Smith", "Evans", "White", "Jones", "Tremblay", "Lee", "Brown", "Miller", "McAllister",
                      "White"]
list_of_countries = ["Poland", "Germany", "France", "Czech Republic", "United States", "Sweden"]

list_of_generated_people = []


def get_unique_random(source_list):
    return source_list.pop(random.randint(0, len(source_list) - 1))


def get_random(source_list):
    return source_list[random.randint(0, len(source_list) - 1)]


def print_personal_data(personal_data):
    print(
        f"Hi! I'm {personal_data['firstname']} {personal_data['lastname']}. I come from {personal_data['country']} and"
        f" I was born in {personal_data['year_of_birth']}.")


def generate_people(count):
    for i in range(0, count):
        first_name = get_unique_random(list_of_women_names)
        last_name = get_unique_random(list_of_last_names)
        country = get_random(list_of_countries)
        email = f'{first_name}.{last_name}@example.com'
        low_letter_email = email.lower()
        age = random.randint(12, 30)
        adultness = age >= 18
        date_of_birth = today().year - age
        personal_data = {
            "firstname": first_name,
            "lastname": last_name,
            "country": country,
            "email": low_letter_email,
            "age": age,
            "adult": adultness,
            "year_of_birth": date_of_birth
        }
        list_of_generated_people.append(personal_data)
        first_name = get_unique_random(list_of_man_names)
        last_name = get_unique_random(list_of_last_names)
        country = get_random(list_of_countries)
        email = f'{first_name}.{last_name}@example.com'
        low_letter_email = email.lower()
        age = random.randint(5, 45)
        adultness = age >= 18
        date_of_birth = today().year - age
        personal_data = {
            "firstname": first_name,
            "lastname": last_name,
            "country": country,
            "email": low_letter_email,
            "age": age,
            "adult": adultness,
            "year_of_birth": date_of_birth
        }
        list_of_generated_people.append(personal_data)


if __name__ == '__main__':
    people_count = 5
    generate_people(people_count)
    for i in range(0, people_count * 2):
        print_personal_data(list_of_generated_people[i])
