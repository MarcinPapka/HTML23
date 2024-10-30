def print_greeting_for_a_person_in_the_city(person_name, city):
    print(f'Witaj {person_name} ! Miło Cię widzieć w naszym mieście: {city}')


def generate_address_email(first_name, last_name):
    print(f'{first_name.lower()}.{last_name.lower()}@4testers.pl')




if __name__ == '__main__':
    # Zadanie 1
    print_greeting_for_a_person_in_the_city("Kasia", "Szczecin")
    print_greeting_for_a_person_in_the_city("Adam", "Poznań")
    # Zadanie 2
    generate_address_email("Janusz", "Nowak")
    generate_address_email("Barbara", "Kowalska")
