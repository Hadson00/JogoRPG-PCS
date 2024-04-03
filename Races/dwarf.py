from character import Character

class Dwarf(Character):
    def __init__(self)-> None:
        super().__init__()
    
    def addAtribute(self):
        self._constitution += 2
        return self._constitution
    
class HillDwarf(Character):
    def __init__(self):
        super().__init__()
    
    def addAtribute(self):
        self._wisdom += 1
        return self._wisdom

class MountainDwarf(Dwarf):
    def __init__(self):
        super().__init__()
    
    def addAtribute(self):
        self._strenght += 2
        return self._strenght