import os
import sys
diretorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(diretorio_raiz)
from character import Character

class Elf(Character):
    def __init__(self, player_name: None, races: None)-> None:
        super().__init__(player_name, races)
        self._dexterity += 2

class HighElf(Elf):
    def __init__(self, player_name: None, races: None)-> None:
        super().__init__(player_name, races)
        self._intelligence += 1
    
class WoodElf(Elf):
    def __init__(self, player_name: None, races: None)-> None:
        super().__init__(player_name, races)
        self._wisdom += 1

class DarkElf(Elf):
    def __init__(self, player_name: None, races: None)-> None:
        super().__init__(player_name, races)
        self._charisma += 1