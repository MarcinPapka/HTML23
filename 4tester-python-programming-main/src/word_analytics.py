
def filter_words_containing_letter_a(list_of_words):
    filtered_words = []
    for word in list_of_words:
        if not isinstance(word, str):
            continue
        if 'a' in word:
            filtered_words.append(word)
    return filtered_words
