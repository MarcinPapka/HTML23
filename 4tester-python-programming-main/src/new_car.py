from datetime import date


class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, distance):
        self.mileage += distance
        return None

    def has_warranty(self):
        current_year = date.today().year
        car_age = current_year - self.year
        return False if car_age > 7 or self.mileage > 120000 else True

    def get_description(self):
        return f'This is a {self.model} made in {self.year}. Currently it drove {self.mileage} kilometers'


if __name__ == '__main__':
    toyota = Car("Yaris", 2020)
    jeep = Car("Wrangler", 2014)

    toyota.drive(25000)
    jeep.drive(160000)

    print(toyota.has_warranty())
    print(jeep.has_warranty())

    print(toyota.get_description())
    print(jeep.get_description())
