class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        print(f"Walking {self.pet.name}")
        self.pet.play()
        return self

    def feed(self):
        print(f"Feeding {self.pet.name} {self.pet_food} and {self.treats}")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"Giving {self.pet.name} a bath")
        self.pet.noise()
        return self
