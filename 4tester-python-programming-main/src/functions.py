def print_word_uppercase(word):
    uppercase_word = word.upper()
    print(uppercase_word)


print_word_uppercase('piesek')
print_word_uppercase('adam')


def is_person_an_adult(age):
    if age >= 18:
        return True
    else:
        return False