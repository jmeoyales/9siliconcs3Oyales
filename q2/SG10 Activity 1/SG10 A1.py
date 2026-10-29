class Animal:
    #creates attribute name for the animal
    def __init__(self, name):
        self.name = name

    #methods of the animal
    #eat funtion
    def eat(self):
        print("Normal Animal eats.")
    #make sound function
    def make_sound(self):
        print("Normal Animal makes sound.")

class lion(Animal):

    def eat(self):
        print(f"{self.name} eats Fresh Meat.")

    def make_sound(self):
        print(f"{self.name} roars loudly!")

class elephant(Animal):D

    def eat(self):
        print(f"{self.name} eats grass and fruits.")

    #An elephant's equivalent to a lion's roar is a trumpet
    def make_sound(self):
        print(f"{self.name} trumpets!")

class monkey(Animal):

    def eat(self):
        print(f"{self.name} eats bananas.")

    def make_sound(self):
        print(f"{self.name} chatters!")


chimp = monkey("George")
king = lion("Simba")
long_nose = elephant("Dumbo")

Animals = [chimp,king,long_nose]

for animal in Animals:
    animal.make_sound()
    animal.eat()
    print("-----")