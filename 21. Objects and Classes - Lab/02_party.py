class Person:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.party = []

    def party_people(self):
        return ", ".join(self.party)

    def total_people(self):
        return len(self.party)

    def add_to_party(self, name):
        self.party.append(name)


my_party = Party()
while True:
    command = input()

    if command == "End":
        break

    my_party.add_to_party(command)

people = my_party.party_people()
total_people = my_party.total_people()

print(f"Going: {people}")
print(f"Total: {total_people}")
