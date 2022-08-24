from random import choice
from tkinter import END
from forca_data_base import *
from forca_functions import *
from time import sleep

dificuldade = easy.copy()
dificuldade_name = 'easy'
menu = True
while menu:
    escolha_menu = escolher_menu(dificuldade_name)

    if escolha_menu == 1:
        if dificuldade_name == 'english':  # INGLÊS
            sys('cls')
            nome = input(f'{WARNING}TYPE YOUR NAME: {ENDC}').title()
            nome = nome[:20]
            fase = 0
            palavras = 0
            dica = 1
            vidas = 6
            letras_escolhidas = []

            sys('cls')
            print(f'{BOLD}WELCOME TO THE HANGMAN GAME {OKGREEN}{nome}{ENDC}\n{BOLD}THINK CAREFULY, IF YOU MESS UP 6 TIMES IT WILL BE {FAIL}GAME OVER!\n{ENDC}')
        else:  # PORTUGÊS
            sys('cls')
            nome = input(f'{WARNING}DIGITE SEU NOME: {ENDC}').title()
            nome = nome[:20]
            fase = 0
            dica = 1
            vidas = 6
            letras_escolhidas = []

            sys('cls')
            print(f'{BOLD}SEJA MUITO BEM VINDO AO JOGO DA FORCA {OKGREEN}{nome}{ENDC}\n{BOLD}PENSE COM CUIDADO, PORQUE SE VACILAR 6 VEZES SERÁ {FAIL}GAME OVER!\n{ENDC}')

        jogo = True
        if dificuldade_name == 'english':  # INGLÊS
            while jogo:
                palavra_escolhida = choice(dificuldade)
                dificuldade.remove(palavra_escolhida)
                palavra_escolhida = remover_acentos(palavra_escolhida).lower()
                
                fase += 1
                vidas = 6
                tam_palavra = len(palavra_escolhida)
                escolha_letra = ''
                contador = 0

                if fase % 5 == 0:
                    dica += 1

                continuar = input(f'\n{WARNING}PRESS ANY KEY TO CONTINUE\n--->{ENDC}')

                sys('cls')
                while True:
                    if len(dificuldade) < 0:
                        print(f'\t\t{OKGREEN}{BOLD}CONGRATULATIONS, YOU GOT ALL WORD CORRECTLY!{ENDC}')
                        print(f'\n\n{BOLD}TRY A DIFFERENT DIFICULTY YOU HAVE NOT COMPLETED YET{ENDC}')
                        continuar = input(f'{WARNING}PRESS ANY KEY TO CONTINUE\n--->{ENDC}')
                        person = [nome, dificuldade_name, fase]
                        insert_one(person)
                        break

                    if vidas == 0:
                        sys('cls')
                        print(f'{FAIL}{BOLD}GAME OVER{ENDC}\nTHE WORD WAS {OKGREEN}{palavra_escolhida.upper()}{ENDC}')
                        sleep(1)
                        print(f'{FAIL}{BOLD}GAME OVER{ENDC}\n{BOLD}YOU GOT TO LEVEL: {OKGREEN}{fase}{ENDC}')
                        continuar = input(f'{WARNING}PRESS ANY KEY TO CONTINUE\n--->{ENDC}')
                        jogo = False
                        person = [nome, dificuldade_name, fase]
                        insert_one(person)
                        break
                    
                    print(f'{HEADER}{BOLD}LIFES: {OKGREEN}{vidas}{ENDC}\t\t{HEADER}LEVEL: {OKGREEN}{fase}{ENDC}\t\t{HEADER}HINT:{ENDC} {OKGREEN}{dica}{ENDC}\t\t{OKGREEN}DIFICULTY: {dificuldade_name}{ENDC}\n')
                    print(f'{BOLD}letters chosen: {FAIL}{letras_escolhidas}{ENDC}')

                    print(f'{BOLD}chosen word: ', end='')
                    contador = 0
                    for i in palavra_escolhida:
                        if i in letras_escolhidas:
                            print(f'{OKGREEN}', i, f'{ENDC}', end=' ')
                            contador += 1
                        else:
                            print(f'{FAIL}_{ENDC}', end=' ')
                
                    if contador == len(palavra_escolhida):
                        print('\n')
                        sys('cls')
                        print(f'{OKGREEN}{BOLD}CONGRATULATIONS, YOU GOT IT RIGHT{ENDC}\nTHE WORD WAS {WARNING}{palavra_escolhida.upper()}{ENDC}')
                        letras_escolhidas.clear()
                        break

                    else:
                        print('\n')
                        print(f'{OKGREEN}[1] HINT{ENDC}')
                        print(f'{FAIL}[0] QUIT{ENDC}')
                        print(f'{WARNING}choose letter', end=' ')
                        escolha_letra = input(f'--->{ENDC}').lower()

                        if escolha_letra == '0':
                            sys('cls')
                            print(f'{BOLD}YOU REALLY WANT TO QUIT?\n{FAIL}[0] QUIT\n{OKGREEN}[any key] CONTINUE{ENDC}')
                            sair = input(f'{WARNING}--->{ENDC}')
                            if sair == '0':
                                jogo = False
                                break
                            else:
                                sys('cls')

                        elif escolha_letra == '1' and dica > 0:
                            for i in palavra_escolhida:
                                if i not in letras_escolhidas:
                                    escolha_letra = i
                                    break
                            dica -= 1
                            sys('cls')
                            print(f'{OKGREEN}HINT: {escolha_letra}{ENDC}')
                            print(f'{BOLD}HINTS LEFT: {FAIL}{dica}{ENDC}')
                            continuar = input(f'{WARNING}PRESS ANY KEY TO CONTINUE\n--->{ENDC}')
                            sys('cls')
                        
                        elif escolha_letra == '1' and dica < 1:
                            print(f'{BOLD}{FAIL}NO HINTS LEFT: {dica}{ENDC}\n')
                            continuar = input(f'{WARNING}PRESS ANY KEY TO CONTINUE\n--->{ENDC}')
                            sys('cls')

                        if escolha_letra == palavra_escolhida:
                            sys('cls')
                            print(f'{OKGREEN}{BOLD}CONGRATULATIONS, YOU GOT IT RIGHT{ENDC}\nTHE WORD WAS {WARNING}{palavra_escolhida.upper()}{ENDC}')
                            letras_escolhidas.clear()
                            break

                        elif len(escolha_letra) == 1 and escolha_letra not in letras_escolhidas and escolha_letra.isnumeric() == False:
                            letras_escolhidas.append(escolha_letra)
                            sys('cls')
                            if escolha_letra not in palavra_escolhida:
                                sys('cls')
                                print(f'{BOLD}THIS WORD DOES NOT HAVE THE LETTER {FAIL}{escolha_letra}{ENDC}\n{BOLD}TRY AGAIN\n{FAIL}{vidas - 1} LIFES LEFT{ENDC}')
                                vidas -= 1
                                sleep(1)
                                sys('cls')

                        elif escolha_letra != palavra_escolhida and len(escolha_letra) == len(palavra_escolhida):
                            sys('cls')
                            print(f'{BOLD}THIS WORD IS NOT {FAIL}{escolha_letra}{ENDC}\n{BOLD}TRY AGAIN\n{ENDC}{FAIL}{vidas - 1} LIFES LEFT{ENDC}')
                            vidas -= 1
                            sleep(1)
                            sys('cls')

                        elif escolha_letra != '0' and escolha_letra != '1':
                            sys('cls')
                            print(f'{FAIL}"{escolha_letra}" INVALID INPUT\nTRY AGAIN{ENDC}')

        else:  # PORTUGUÊS
            while jogo:
                palavra_escolhida = choice(dificuldade)
                dificuldade.remove(palavra_escolhida)
                palavra_escolhida = remover_acentos(palavra_escolhida).lower()
                
                fase += 1
                vidas = 6
                tam_palavra = len(palavra_escolhida)
                escolha_letra = ''
                contador = 0

                if fase % 5 == 0:
                    dica += 1

                continuar = input(f'{WARNING}\nPRESSIONE QUALQUER TECLA PARA CONTINUAR\n--->{ENDC}')

                sys('cls')
                while True:
                    if len(dificuldade) < 0:
                        print(f'\t\t{OKGREEN}{BOLD}PARABÉN, VOCÊ ACERTOU TODAS AS PALAVARS!{ENDC}')
                        print(f'\n\n{BOLD}TENTE UMA DIFICULDADE DIFERENTE QUE VOCE NÃO TENHA COMPLETADO AINDA{ENDC}')
                        continuar = input(f'{WARNING}PRESSIONE QUALQUER TECLA PARA CONTINUAR\n--->{ENDC}')
                        person = [nome, dificuldade_name, fase]
                        insert_one(person)
                        break

                    if vidas == 0:
                        sys('cls')
                        print(f'{FAIL}{BOLD}GAME OVER{ENDC}\nA PALAVRA ERA {OKGREEN}{palavra_escolhida.upper()}{ENDC}')
                        sleep(1)
                        print(f'{FAIL}{BOLD}GAME OVER{ENDC}\n{BOLD}VOCÊ CHEGOU ATÉ A FASE: {OKGREEN}{fase}{ENDC}')
                        continuar = input(f'{WARNING}PRESSIONE QUALQUER TECLA PARA CONTINUAR\n--->{ENDC}')
                        jogo = False
                        person = [nome, dificuldade_name, fase]
                        insert_one(person)
                        break
                    
                    print(f'{HEADER}{BOLD}VIDAS: {OKGREEN}{vidas}{ENDC}\t\t{HEADER}FASE: {OKGREEN}{fase}{ENDC}\t\t{HEADER}DICAS:{ENDC}{OKGREEN} {dica}{ENDC}\t\t{OKGREEN}NÍVEL: {dificuldade_name}{ENDC}\n')
                    print(f'{BOLD}letras escolhidas: {FAIL}{letras_escolhidas}{ENDC}')

                    print(f'{BOLD}palavra escolhida: ', end='')
                    contador = 0
                    for i in palavra_escolhida:
                        if i in letras_escolhidas:
                            print(f'{OKGREEN}', i, f'{ENDC}', end=' ')
                            contador += 1
                        else:
                            print(f'{FAIL}_{ENDC}', end=' ')
                
                    if contador == len(palavra_escolhida):
                        print('\n')
                        sys('cls')
                        print(f'{OKGREEN}{BOLD}PARABÉNS, VOCÊ ACEROU!{ENDC}\nA PALAVRA ERA {WARNING}{palavra_escolhida.upper()}{ENDC}')
                        letras_escolhidas.clear()
                        break

                    else:
                        print('\n')
                        print(f'{OKGREEN}[1] DICA{ENDC}')
                        print(f'{FAIL}[0] QUIT{ENDC}')
                        print(f'{WARNING}escolha letra', end=' ')
                        escolha_letra = input(f'--->{ENDC}').lower()

                        if escolha_letra == '0':
                            sys('cls')
                            print(f'{BOLD}DESEJA REALMENTE SAIR DA PARTIDA?\n{FAIL}[0] QUIT\n{OKGREEN}[qualquer tecla] CONTINUAR{ENDC}')
                            sair = input(f'{WARNING}--->{ENDC}')
                            if sair == '0':
                                jogo = False
                                break
                            else:
                                sys('cls')
                        
                        elif escolha_letra == '1' and dica > 0:
                            for i in palavra_escolhida:
                                if i not in letras_escolhidas:
                                    escolha_letra = i
                                    break
                            dica -= 1
                            sys('cls')
                            print(f'{OKGREEN}DICA: {escolha_letra}{ENDC}')
                            print(f'{BOLD}DICAS RESTANTES: {FAIL}{dica}{ENDC}')
                            continuar = input(f'{WARNING}\nPRESSIONE QUALQUER TECLA PARA CONTINUAR\n--->{ENDC}')
                            sys('cls')
                        
                        elif escolha_letra == '1' and dica < 1:
                            print(f'{BOLD}{FAIL}SEM DICAS SOBRANDO: {dica}{ENDC}\n')
                            continuar = input(f'{WARNING}\nPRESSIONE QUALQUER TECLA PARA CONTINUAR\n--->{ENDC}')
                            sys('cls')

                        if escolha_letra == palavra_escolhida:
                            print('\n')
                            sys('cls')
                            print(f'{OKGREEN}{BOLD}PARABÉNS, VOCÊ ACEROU!{ENDC}\nA PALAVRA ERA {WARNING}{palavra_escolhida.upper()}{ENDC}')
                            letras_escolhidas.clear()
                            break

                        elif len(escolha_letra) == 1 and escolha_letra not in letras_escolhidas and escolha_letra.isnumeric() == False:
                            letras_escolhidas.append(escolha_letra)
                            sys('cls')
                            if escolha_letra not in palavra_escolhida:
                                sys('cls')
                                print(f'{BOLD}ESSA PALAVRA NÃO POSSUI A LETRA {FAIL}{escolha_letra}{ENDC}\n{BOLD}TENTE NOVAMENTE\n{FAIL}{vidas - 1} VIDAS RESTANTES{ENDC}')
                                vidas -= 1
                                sleep(1)
                                sys('cls')

                        elif escolha_letra != palavra_escolhida and len(escolha_letra) == len(palavra_escolhida):
                            sys('cls')
                            print(f'{BOLD}ESSA PALAVRA NÃO É {FAIL}{escolha_letra}{ENDC}\n{BOLD}TENTE NOVAMENTE\n{ENDC}{FAIL}{vidas - 1} VIDAS RESTANTES{ENDC}')
                            vidas -= 1
                            sleep(1)
                            sys('cls')

                        elif escolha_letra != '0':
                            sys('cls')
                            print(f'{FAIL}"{escolha_letra}" INPUT INVÁLIDO\nTENTE NOVAMENTE{ENDC}')

    elif escolha_menu == 2:
        dificuldade, dificuldade_name = escolher_dificuldade(dificuldade, dificuldade_name)

    elif escolha_menu == 3:
        regras(dificuldade_name)

    elif escolha_menu == 4:
        ranking_list = get_all()
        ranking(ranking_list, dificuldade_name)

    elif escolha_menu == 5:
        if dificuldade_name == 'english':  #INGLÊS
            sys('cls')
            print(f'\t\t{HEADER}{BOLD}THANKS TO PLAY!{ENDC}')
            menu = False
            
        else:  # PORTUGÊS
            sys('cls')
            print(f'\t\t{HEADER}{BOLD}OBRIGADO POR JOGAR!{ENDC}')
            menu = False
