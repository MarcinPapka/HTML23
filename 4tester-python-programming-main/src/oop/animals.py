class Dog:

    def __init__(self, name):
        self.name = name
        self.age = 0
        self.food_in_belly = 0

    def feed(self, amount_of_food):
        self.food_in_belly += amount_of_food

    def poop(self, weight_of_poppy):
        self.food_in_belly -= weight_of_poppy


if __name__ == '__main__':
    dog1 = Dog('Amik')
    dog2 = Dog('Panela')
    print(dog1.name)
    print(dog2.name)
    dog1.name = 'Azor'
    dog2.name = 'Bobi'
    print(dog1.name)
    print(dog2.name)
    print(dog2.age)

    print(dog1.food_in_belly)
    dog1.feed(100)
    print(dog1.food_in_belly)
    dog1.feed(100)
    print(dog1.food_in_belly)
    dog1.poop(50)
    print(dog1.food_in_belly)
