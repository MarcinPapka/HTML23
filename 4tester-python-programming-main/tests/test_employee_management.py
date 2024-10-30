from src.employee_management import generate_seniority_years


def test_generate_seniority_years_are_in_proper_range():
    test_seniority_years = generate_seniority_years()
    assert test_seniority_years >=0
    assert test_seniority_years <=40
    assert isinstance(test_seniority_years, int)


