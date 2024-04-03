from character import Character

class Barbarian(Character):
    def __init__(self, races):
        super().__init__(races)
    
    def addAtribute(self):
        self._dexterity += 2
        return self._dexterity

class Lightfoot(Barbarian):
    def __init__(self, races):
        super().__init__(races)
    
    def addAtribute(self):
        self._charisma + 1
        return self._charisma

class Stout(Barbarian):
    def __init__(self, races):
        super().__init__(races)
    
    def addAtribute(self):
        self._constitution + 1
        return self._constitution