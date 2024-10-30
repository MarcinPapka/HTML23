from src.word_analytics import filter_words_containing_letter_a


def test_filtering_words_for_empty_list():
    filtered_list = filter_words_containing_letter_a([])
    assert filtered_list == []


def test_filtering_words_for_list_of_integes():
    filtered_list = filter_words_containing_letter_a([1, 2, 3])
    assert filtered_list == []


def test_filtering_words_for_list_of_special_characters():
    filtered_list = filter_words_containing_letter_a(['@', '#'])
    assert filtered_list == []


def test_filtering_words_for_list_not_containing_any_word_with_letter_a():
    filtered_list = filter_words_containing_letter_a(['pies', 'smok', 'kot'])
    assert filtered_list == []


def test_filtering_words_for_mixed_list_of_single_values():
    filtered_list = filter_words_containing_letter_a([1, 'a', 'b', 'a'])
    assert filtered_list == ['a', 'a']
