class Zoo:
    __animals = 0

    def __init__(self, name) -> None:
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"{species.capitalize()}s in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"{species.capitalize()}es in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"{species.capitalize()}s in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
animal_number = int(input())

zoo = Zoo(zoo_name)

for animal in range(animal_number):
    specie, type_of_animal = input().split()
    zoo.add_animal(specie, type_of_animal)

needed_specie = input()

print(zoo.get_info(needed_specie))
