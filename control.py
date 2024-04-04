from Races.barbarian import *
from Races.dragonborn import *
from Races.dwarf import *
from Races.elf import *
from Races.gnome import *
from Races.human import *
from Races.tiefling import *
from character import *

class Control:
    while True:
        print('_________Bem Vindo Ao RPG_________\n')
        try:
            selector = (int(input('Digite 1 para criar seu personagem \n'
                                  'Digite 2 para finalizar o jogo \n'
                                  'Selecione: \n')))
            if selector == 1:
                player_name = str(input('Digite o nome do seu personagem: '))
                print('--------------------------------')
                print('_________Escolha sua raça_________\n')
                player_race = (int(input('0: Anão\n'
                                        '1: Elfo\n'
                                        '2: Bárbaro\n'
                                        '3: Humano\n'
                                        '4: Draconato\n'
                                        '5: Gnomo\n'
                                        '6: Ladrão\n'
                                        'Selecione: ')))
                races = ['Anão', 'Elfo', 'Bárbaro', 'Humano', 'Draconato', 'Gnomo', 'Ladrão'] #Todas as raças
                match player_race: #Implementar player_race em races
                    case 0:
                        print('_________Escolher Sub-Raça_________')
                        player_race = (int(input('0: Anão da colina\n'
                                                '1: Anão da montanha\n'
                                                '2: Sem troca de raça\n'
                                                'Selecione: ')))
                        races = ['Anão da colina', 'Anão da montanha','Anão']
                        match player_race:
                            case 0:
                                player_character = HillDwarf(player_name, races[player_race])
                            case 1:
                                player_character = MountainDwarf(player_name, races[player_race])
                            case 2:
                                player_character = Dwarf(player_name, races[player_race])
                            case _:
                                print('Erro -> Número inválido')
                    case 1: 
                        print('\n_________Deseja uma Sub-Raça_________')
                        player_race = (int(input('0: Elfo Alto\n'
                                                '1: Elfo da floresta\n'
                                                '2: Elfo negro\n'
                                                '3: Sem troca de raça\n'
                                                'Selecione: ')))
                        races = ['Elfo Alto', 'Elfo da floresta','Elfo negro', 'Elfo']
                        match player_race:
                            case 0:
                                player_character = HighElf(player_name, races[player_race])
                            case 1:
                                player_character = WoodElf(player_name, races[player_race])
                            case 2:
                                player_character = DarkElf(player_name, races[player_race])
                            case 3:
                                player_character = Elf(player_name, races[player_race])
                            case _:
                                print('Erro -> Número inválido')

                    case 2: 
                        print('_________Escolher Sub-Raça_________')
                        player_race = (int(input('0: Bárbaro Veloz\n'
                                                 '1: Bárbaro Robusto\n'
                                                 '2: Sem troca de raça\n'
                                                 'Selecione: ')))
                        races = ['Bárbaro Veloz', 'Bárbaro Robusto','Bárbaro']
                        match player_race:
                            case 0:
                                player_character = Lightfoot(player_name, races[player_race])
                            case 1: 
                                player_character = Stout(player_name, races[player_race])
                            case 2:
                                player_character = Barbarian(player_name, races[player_race])
                            case _:
                                print('Erro -> Número inválido')

                    case 3: 
                        player_character = Human(player_name, races[player_race])

                    case 4:
                        player_character = Dragonborn(player_name, races[player_race])

                    case 5: 
                        print('_________Escolher Sub-Raça_________')
                        player_race = (int(input('0: Gnomo da floresta\n'
                                                 '1: Gnomo da pedra\n'
                                                 '2: Sem troca de raça\n'
                                                 'Selecione: ')))
                        races = ['Gnomo da floresta', 'Gnomo da pedra','Gnomo']
                        match player_race:
                            case 0:
                                player_character = ForestGnome(player_name, races[player_race])
                            case 1: 
                                player_character = RockGnome(player_name, races[player_race])
                            case 2:
                                player_character = Gnome(player_name, races[player_race])
                            case _:
                                print('Erro -> Número inválido')
                        
                    case 6: 
                        player_character = Tiefling(player_name, races[player_race])

                print(player_character)

            elif selector == 2:
                    break

            else: 
                print('Error')
                break
        except:
            print('Erro -> Seletor incorreto')