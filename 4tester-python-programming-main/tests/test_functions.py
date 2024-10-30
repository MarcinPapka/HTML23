from src.functions import is_person_an_adult

def test_check_person_under_adult_age():
    test_is_adult = is_person_an_adult(17)
    assert not test_is_adult

def test_check_person_equal_adult_age():
    test_is_adult = is_person_an_adult(18)
    assert test_is_adult

def test_check_person_above_adult_age():
    test_is_adult = is_person_an_adult(19)
    assert test_is_adult

