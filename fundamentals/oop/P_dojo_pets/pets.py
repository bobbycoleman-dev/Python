class Pet:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("BARK BARK BARK")


# SENSEI BONUS
class Dog(Pet):
    def __init__(self, name, type, breed, tricks, health, energy):
        super().__init__(name, type)
        self.breed = breed
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        return super().sleep()

    def eat(self):
        return super().eat()

    def play(self):
        return super().play()

    def noise(self):
        return super().noise()
