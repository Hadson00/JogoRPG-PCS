import os
import sys
diretorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(diretorio_raiz)
from character import Character

class Barbarian(Character):
    def __init__(self, player_name: None, races: None)-> None:
        super().__init__(player_name, races)
        self._dexterity += 2

class Lightfoot(Barbarian):
    def __init__(self, player_name: None, races: None)-> None:
        super().__init__(player_name, races)
        self._charisma + 1

class Stout(Barbarian):
    def __init__(self, player_name: None, races: None)-> None:
        super().__init__(player_name, races)
        self._constitution + 1