from character import *

class Gnome(Character):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._intelligence + 2

class ForestGnome(Gnome):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._dexterity + 1

class RockElf(Gnome):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._constitution + 1