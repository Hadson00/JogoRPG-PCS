from character import Character

class Dragonborn(Character):
    def __init__(self, races):
        super().__init__(races)
    
    def addAtribute(self):
        self._strenght += 2
        self._charisma += 1
        return self._strenght, self._charisma