from ..character import Character

class Human(Character):
    def __init__(self, races):
        super().__init__(races)
    
    def addAtribute(self):
        self._strenght += 1
        self._dexterity += 1 
        self._constitution += 1
        self._wisdom += 1
        self._intelligence += 1
        self._charisma += 1
        return self._strenght, self._dexterity, self._constitution, self._wisdom, self._intelligence, self._charisma