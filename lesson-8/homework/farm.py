class Animal:
    # Initialize an animal with a name, species, and sound
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    # Method to return the sound the animal makes
    def make_sound(self):
        return f"{self.name} the {self.species} says '{self.sound}'"

    # Method to simulate the animal eating
    def eat(self, food):
        return f"{self.name} is eating {food}."

    # Method to simulate the animal sleeping
    def sleep(self):
        return f"{self.name} is sleeping."


class Cow(Animal):
    # Initialize a Cow with a default species and sound
    def __init__(self, name):
        super().__init__(name, "Cow", "Moo")

    # Method to simulate milk production
    def produce_milk(self):
        return f"{self.name} is producing milk."


class Chicken(Animal):
    # Initialize a Chicken with a default species and sound
    def __init__(self, name):
        super().__init__(name, "Chicken", "Cluck")

    # Method to simulate egg laying
    def lay_egg(self):
        return f"{self.name} has laid an egg."


class Sheep(Animal):
    # Initialize a Sheep with a default species and sound
    def __init__(self, name):
        super().__init__(name, "Sheep", "Baa")

    # Method to simulate shearing wool
    def shear_wool(self):
        return f"{self.name} has been sheared for wool."


# Example usage:
cow = Cow("Bessie")
chicken = Chicken("Clucky")
sheep = Sheep("Wooly")

# Store animals in a list
animals = [cow, chicken, sheep]

# Iterate through the list and print details about each animal
for animal in animals:
    print(animal.make_sound())  # Print the sound the animal makes
    print(animal.eat("grass"))  # Print what the animal is eating
    print(animal.sleep())  # Print that the animal is sleeping
    
# Print specific actions for each type of animal
print(cow.produce_milk())  # Cow produces milk
print(chicken.lay_egg())  # Chicken lays an egg
print(sheep.shear_wool())  # Sheep gets sheared
