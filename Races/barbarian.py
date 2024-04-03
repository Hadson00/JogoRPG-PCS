from character import Character

class Barbarian(Character):
    def __init__(self):
        super().__init__()
    
    def addAtribute(self):
        self._dexterity += 2
        return self._dexterity

class Lightfoot(Barbarian):
    def __init__(self):
        super().__init__()
    
    def addAtribute(self):
        self._charisma + 1
        return self._charisma

class Stout(Barbarian):
    def __init__(self):
        super().__init__()
    
    def addAtribute(self):
        self._constitution + 1
        return self._constitution