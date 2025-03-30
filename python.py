from abc import ABC,abstractmethod

class Pokemon(ABC):
    def __init__(self,name,level,type):
        self.name = name
        self.level = level
        self.type = type
        self.health = level * 10

    def skills_used(self):
        print(self.name,"Used his skills")

    @abstractmethod
    def take_damage(self):
        pass

    def heal(self):
        self.health += 10
        print(f"{self.name} healed !")

    def show_details(self):
        print(f"name : {self.name}")
        print(f"level : {self.level}")
        print(f"type : {self.type}")
        print(f"health : {self.health}")

class ElectricPokemon(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level,type = "Electric")

    def thunderbolt(self):
        self.skills_used()
        print(f"{self.name} used special skill : Thunderbolt !")

    def skills_used(self):
        print(f"{self.name} used Electricity !")

    def take_damage(self):
        self.health -= 30
        if self.health < 0:
            print(f"{self.name} fainted !")

class WaterPokemon(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level,type = "Water")

    def Bubble_Beam(self):
        self.skills_used()
        print(f"{self.name} used special skill : Bubble Beam !")

    def skills_used(self):
        print(f"{self.name} used Water !")

    def take_damage(self):
        self.health -= 25
        if self.health < 0:
            print(f"{self.name} fainted !")


class FirePokemon(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level,type = "Fire")

    def Blast_Burn(self):
        self.skills_used()
        print(f"{self.name} used special skill : Blast Burn !")

    def skills_used(self):
        print(f"{self.name} used fire !")

    def take_damage(self):
        self.health -= 45
        if self.health < 0:
            print(f"{self.name} fainted !")

# For electric pokemon
pikachu = ElectricPokemon("Pikachu", 20)
pikachu.show_details()
print()

# For Fire pokemon
charizard = FirePokemon("Charizard",35)
charizard.show_details()
print()

print("Pikachu v/s Charizard")
while True:
    print("------------Battle Starts------------")
    print(f"{pikachu.name} is here")
    pikachu.thunderbolt()
    print()
    charizard.take_damage()
    print()
    print(f"{charizard.name} is here")
    print()
    charizard.Blast_Burn()
    print()
    pikachu.take_damage()
    print(f"{pikachu.name}'s health : {pikachu.health}")
    if charizard.health < 0 or pikachu.health < 0 :
        break
    print("\n")

'''
pikachu = ElectricPokemon("Pikachu", 20)
pikachu.show_details()
print()

# Water Pokemon
squirtle = WaterPokemon("Squirtle",15)
squirtle.Bubble_Beam()
squirtle.show_details()

print("Calling skills used method")
pikachu.skills_used()
print()
squirtle.take_damage()
print()
squirtle.Bubble_Beam()
print()
pikachu.take_damage()

print("After using the skills")
pikachu.show_details()
print()
squirtle.show_details()
print()

# Fire pokemon
charizard = FirePokemon("Charizard",35)
charizard.show_details()
print()
charizard.skills_used()
print()
charizard.take_damage()
print("After using skills")
charizard.show_details()





'''
