from character import Character

class Tiefling(Character):
    def __init__(self, races)-> None:
        super().__init__(races)
    
    def addAtribute(self):
        self._intelligence += 1
        self._charisma += 2
        return self._intelligence, self._charisma