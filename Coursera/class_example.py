class PartyAnimal:
    x = 0

    def __init__(self):
        print("Constructed")

    def __del__(self):
        print("Destructed")

    def party(self) :
        self.x = self.x + 1
        print("So far",self.x)


an = PartyAnimal()

an.party()
an.party()
an.party()
print(type(an))
print(dir(an))
str()
an = 42
print(an)
