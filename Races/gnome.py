from character import Character

class Gnome(Character):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._intelligence += 2
        return self._intelligence

class ForestGnome(Gnome):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._dexterity += 1
        return self._dexterity

class RockGnome(Gnome):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._constitution += 1
        return self._constitution