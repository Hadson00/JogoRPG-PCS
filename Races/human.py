from character import *

class Human(Character):
    def __init__(self):
        super().__init__()
    
    def addAtribute(self):
        self._strenght + 1
        self._dexterity + 1 
        self._constitution + 1
        self._wisdom + 1
        self._intelligence + 1
        self._charisma + 1