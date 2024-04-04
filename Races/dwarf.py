import os
import sys
diretorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(diretorio_raiz)
from character import Character

class Dwarf(Character):
    def __init__(self, player_name: None, races: None)-> None:
        super().__init__(player_name, races)
        self._constitution += 2
    
class HillDwarf(Dwarf):
    def __init__(self, player_name: None, races: None)-> None:
        super().__init__(player_name, races)
        self._wisdom += 1

class MountainDwarf(Dwarf):
    def __init__(self, player_name: None, races: None)-> None:
        super().__init__(player_name, races)
        self._strenght += 2