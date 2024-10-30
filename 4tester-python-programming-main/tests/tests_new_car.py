from src.new_car import Car


def test_if_newly_created_car_has_zero_mileage():
    car = Car("Cinquecento", 1990)
    assert car.mileage == 0


def test_if_mileage_is_100_after_driving_100_kilometers():
    car = Car("Cinquecento", 1990)
    car.drive(100)
    assert car.mileage == 100


def test_if_mileage_is_300_after_driving_100_and_200_kilometers():
    car = Car("Cinquecento", 1990)
    car.drive(100)
    car.drive(200)
    assert car.mileage == 300


def test_if_2020_model_with_mileage_of_119000_has_warranty():
    car = Car("Cinquecento", 2020)
    car.drive(119000)
    assert car.has_warranty()


def test_if_2007_model_with_mileage_of_19000_has_no_warranty():
    car = Car("Cinquecento", 2007)
    car.drive(19000)
    assert not car.has_warranty()


def test_if_1998_honda_civic_with_mileage_230000_description_is_correct():
    car = Car("Honda Civic", 1998)
    car.drive(230000)
    expected_description = "This is a Honda Civic made in 1998. Currently it drove 230000 kilometers"
    actual_description = car.get_description()
    assert expected_description == actual_description
