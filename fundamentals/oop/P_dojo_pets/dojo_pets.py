import ninja, pets

# pet = pets.Pet("Cooper", "Dog", "Shake", 85, 70)
# SENSEI BONUS
pet = pets.Dog("Cooper", "Dog", "GSP", "Shake", 85, 70)
ninja = ninja.Ninja("Bobby", "Coleman", pet, "Milk Bones", "Kibble")

ninja.feed().walk().bathe()
print(pet.energy)
print(pet.health)
pet.sleep()
print(pet.energy)
