import random

class Character:
    def __init__(self, player_name: None, races: None)-> None:
        self.player_name = player_name
        self.races = races
        self._type_strenght = {
            'Incorpóreo':[0],
            'Incapaz':[1,2,3,4,5],
            'Fraco':[6,7,8,9],
            'Mediano':[10,11],
            'Forte':[12,13,14,15],
            'Super Poderoso':[16,17,18,19,20],
            'Imbatível':[21]
        }
        self._type_decterity = {
            'Desacordado':[0],
            'Abatido':[1,2,3,4,5],
            'Desajeitado':[6,7,8,9],
            'Regular':[10,11],
            'Ágil':[12,13,14,15],
            'Ninja':[16,17,18,19,20],
            'Imperceptível':[21]
        }
        self._type_constitution = {
            'Espectro':[0],
            'Enfermo':[1,2,3,4,5],
            'Frágil':[6,7,8,9],
            'Saudável':[10,11],
            'Durão':[12,13,14,15],
            'Super Resistente':[16,17,18,19,20],
            'Imortal':[21]
        }
        self._type_wisdom = {
            'Inconsciente':[0],
            'Irracional':[1,2,3,4,5],
            'Desatento':[6,7,8,9],
            'Simples':[10,11],
            'Perspicaz':[12,13,14,15],
            'Filósfo':[16,17,18,19,20],
            'Iluminado':[21]
        }
        self._type_intelligence = {
            'Inanimado':[0],
            'Incivilizado':[1,2,3,4,5],
            'Parvo':[6,7,8,9],
            'Medíocre':[10,11],
            'Estudado':[12,13,14,15],
            'Gênio':[16,17,18,19,20],
            'Onisciente':[21]
        }
        self._type_charisma = {
            'Aberração':[0],
            'Inexpressivo':[1,2,3,4,5],
            'Rude':[6,7,8,9],
            'Sociável':[10,11],
            'Persuasivo':[12,13,14,15],
            'Influente':[16,17,18,19,20],
            'Ídolo':[21]
        }
        self._strenght = random.randint(0,21) #Atributo força
        self._dexterity = random.randint(0,21) #Atributo destreza
        self._constitution = random.randint(0,21) #Atributo constituição
        self._wisdom = random.randint(0,21) #Atributo sabedoria
        self._intelligence = random.randint(0,21) #Atributo inteligência
        self._charisma = random.randint(0,21) #Atributo carisma

    def __calcAtribute(self, value, dic)-> None:
        for x in dic:
            for y in dic[x]:
                if value == y:
                    return x
    
    def typeStrenght(self)-> None:
        return self.__calcAtribute(self._strenght, self._type_strenght)

    def typeDexterity(self)-> None:
        return self.__calcAtribute(self._dexterity, self._type_decterity)

    def typeConstitution(self)-> None:
        return self.__calcAtribute(self._constitution, self._type_constitution)

    def typeWisdom(self)-> None:
        return self.__calcAtribute(self._wisdom, self._type_wisdom)
    
    def typeIntelligence(self)-> None:
        return self.__calcAtribute(self._intelligence, self._type_intelligence)
    
    def typeCharisma(self)-> None:
        return self.__calcAtribute(self._charisma, self._type_charisma)
    
    def __str__(self)-> None: #Printa Personagem
        return (f'\n_________Sobre_________\n\n'
            f'Nome do personagem: {self.player_name}\n'
            f'Raça: {self.races}\n\n'
            f'_________Atributos_________\n\n'
            f'Força: {self._strenght} ({self.typeStrenght()})\n'
            f'Destreza: {self._dexterity} ({self.typeDexterity()})\n'
            f'Constituição: {self._constitution} ({self.typeConstitution()})\n'
            f'Sabedoria: {self._wisdom} ({self.typeWisdom()})\n'
            f'Inteligência: {self._intelligence} ({self.typeIntelligence()})\n'
            f'Carisma: {self._charisma} ({self.typeCharisma()})\n\n'
            )