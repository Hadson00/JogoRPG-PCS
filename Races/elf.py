from character import Character

class Elf(Character):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._dexterity += 2
        return self._dexterity

class HighElf(Elf):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._intelligence += 1
        return self._intelligence
    
class WoodElf(Elf):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._wisdom += 1
        return self._wisdom

class DarkElf(Elf):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._charisma += 1
        return self._charisma