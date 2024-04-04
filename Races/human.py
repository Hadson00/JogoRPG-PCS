import os
import sys
diretorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(diretorio_raiz)
from character import Character

class Human(Character):
    def __init__(self, player_name: None, races: None)-> None:
        super().__init__(player_name, races)
        self._strenght += 1
        self._dexterity += 1 
        self._constitution += 1
        self._wisdom += 1
        self._intelligence += 1
        self._charisma += 1