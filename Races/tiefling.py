from character import *

class Tiefling(Character):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._intelligence + 1
        self._charisma + 2