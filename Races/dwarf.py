#começando racas
#raças precisam receber os atributos
from character import *

class Dwarf(Character):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._constitution + 2
    
class HillDwarf(Character):
    def __init__(self):
        super().__init__()
    
    def addAtribute(self):
        self._wisdom + 1

class MountainDwarf(Dwarf):
    def __init__(self):
        super().__init__()
    
    def addAtribute(self):
        self._strenght + 2