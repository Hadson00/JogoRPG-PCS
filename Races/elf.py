from character import *

class Elf(Character):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._dexterity + 2

class HighElf(Elf):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._intelligence + 1
    
class WoodElf(Elf):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._wisdom + 1

class DarkElf(Elf):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._charisma + 1