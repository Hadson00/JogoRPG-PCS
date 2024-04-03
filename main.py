from Races.barbarian import *
from Races.dragonborn import *
from Races.dwarf import *
from Races.elf import *
from Races.gnome import *
from Races.human import *
from Races.tiefling import *
from character import *

while True:
    print('Bem Vindo Ao RPG Do Titio Igor')
    
    x = int(input('Digite 1 para criar seu personagem\nDigite 2 para finalizar o jogo'))
    if x == 1:
        player_name = str(input('Digite o nome do seu player_character: '))
        print('--------------------------------')
        print('_________Criando sua raça_________')
        player_race = int(input("0: Anão\n1: Elfo\n2: Bárbaro\n3: Humano\n4: Draconato\n5: Gnomo\n6: Ladrão"))
        races = ['Anão', 'Elfo', 'Bárbaro', 'Humano', 'Draconato', 'Gnomo', 'Ladrão']
        match player_race:
            case 0 :
                print('_________Escolher Sub-Raça_________')
                player_race = int(input('0: Anão da colina\n1: Anão da montanha\n2: Sem troca de raça'))
                races = ['Anão da colina", "Anão da montanha","Anão']
                match player_race:
                    case 0 :
                        player_character = HillDwarf(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])
                    case 1 : 
                        player_character = MountainDwarf(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])
                    case 2 :
                        player_character = Dwarf(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])
                            
            case 1: 
                print('_________Escolher Sub-Raça_________')
                player_race = int(input('0: Elfo Alto\n1: Elfo da floresta\n2: Elfo negro\n3: Sem troca de raça'))
                races = ['Elfo Alto', 'Elfo da floresta','Elfo negro', 'Elfo']
                match player_race:
                    case 0 :
                        player_character = HighElf(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])
                    case 1 : 
                        player_character = WoodElf(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])
                    case 2 :
                        player_character = DarkElf(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])
                    case 3 :
                        player_character = Elf(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])

            case 2: 
                print('_________Escolher Sub-Raça_________')
                player_race = int(input('0: Bárbaro Veloz\n1: Bárbaro Robusto\n2: Sem troca de raça'))
                races = ['Bárbaro Veloz', 'Bárbaro Robusto','Bárbaro']
                match player_race:
                    case 0 :
                        player_character = Lightfoot(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])
                    case 1 : 
                        player_character = Stout(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])
                    case 2 :
                        player_character = Barbarian(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])

            case 3: 
                player_character = Human(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])
                
            case 4: 
                player_character = Dragonborn(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])
                
            case 5: 
                print('_________Escolher Sub-Raça_________')
                player_race = int(input('0: Gnomo da floresta\n1: Gnomo da pedra\n2: Sem troca de raça'))
                races = ['Gnomo da floresta', 'Gnomo da pedra','Gnomo']
                match player_race:
                    case 0 :
                        player_character = ForestGnome(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])
                    case 1 : 
                        player_character = RockGnome(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])
                    case 2 :
                        player_character = Gnome(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])
                
            case 6: 
                player_character = Tiefling(player_name, 0, 0, 0, 0, 0, 0, 0, races[player_race])

        #player_character.create_random_weight()    
        print(player_character)

    elif x == 2:
            break

    else: 
        print('Error')
        break

#case _:
#    print("|Erro: Número invalido")     