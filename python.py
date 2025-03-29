from abc import ABC,abstractmethod

class Pokemon(ABC):
    def __init__(self,name,level,Type):
        self.name = name
        self.level = level
        self.Type = Type

    def skills_used(self):
        print(self.name,"Used his skills")

    @abstractmethod
    def take_damage(self):
        pass