from character import *

class Barbarian(Character):
    def __init__(self):
        super().__init__()
    
    def addAtribute(self):
        self._dexterity + 2

class Lightfoot(Barbarian):
    def __init__(self):
        super().__init__()
    
    def addAtribute(self):
        self._charisma + 1

class Stout(Barbarian):
    def __init__(self):
        super().__init__()
    
    def addAtribute(self):
        self._constitution + 1