from requests import head
from forca_words import *
from os import system as sys
from unicodedata import normalize

def remover_acentos(text):
    return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')

def escolher_menu(dificuldade_name):
    sys('cls')
    if dificuldade_name == 'english':
        while True:
            try:
                print(f'\t\t{HEADER}{BOLD}HANGMAN{ENDC}\n\n\t{BOLD}[1] PLAY\n\t[2] SELECT DIFICULTY {OKGREEN}(current - {dificuldade_name.upper()}){ENDC}\n\t[3] GAME RULES\n\t[4] RANKING\n\t{FAIL}[5] QUIT\n{ENDC}')
                escolha_menu = int(input(f'{WARNING}--->{ENDC}'))
                break
            except ValueError:
                sys('cls')
                print(f'{FAIL}typed input must be integer, try again{ENDC}')
    else:
        while True:
            try:
                print(f'\t\t{HEADER}{BOLD}JOGO DA FORCA{ENDC}\n\n\t{BOLD}[1] INICIAR JOGO\n\t[2] SELECIONAR DIFICULDADE {OKGREEN}(atual - {dificuldade_name.upper()}){ENDC}\n\t[3] REGRAS DO JOGO\n\t[4] RANKING\n\t{FAIL}[5] QUIT\n{ENDC}')
                escolha_menu = int(input(f'{WARNING}--->{ENDC}'))
                break
            except ValueError:
                sys('cls')
                print(f'{FAIL}Valor digitado deve ser inteiro, tente novamente{ENDC}')
        
    return escolha_menu

def escolher_dificuldade(dificuldade, dificuldade_name):
    sys('cls')
    if dificuldade_name == 'english':
        while True:
            try:
                print(f'\t\t{HEADER}{BOLD}IN WITCH DIFICULTY YOU WANT TO PLAY?{ENDC}\n\n\t{OKGREEN}current dificulty - {dificuldade_name.upper()}{ENDC}\n\t{BOLD}[1] EAZY\n\t[2] MEDIUM\n\t[3] HARD\n\t[4] ENGLISH\n\n\t[5] MAIN MENU\n{ENDC}')
                escolha_dificuldade = int(input(f'{WARNING}--->{ENDC}'))
                break
            except ValueError:
                sys('cls')
                print(f'{FAIL}typed input must be integer, try again{ENDC}')
    else:
        while True:
            try:
                print(f'\t\t{HEADER}{BOLD}EM QUAL DIFICULDADE DESEJA JOGAR?{ENDC}\n\n\t{OKGREEN}dificuldade atual - {dificuldade_name.upper()}{ENDC}\n\t{BOLD}[1] EAZY\n\t[2] MEDIUM\n\t[3] HARD\n\t[4] ENGLISH\n\n\t[5] VOLTAR\n{ENDC}')
                escolha_dificuldade = int(input(f'{WARNING}--->{ENDC}'))
                break
            except ValueError:
                sys('cls')
                print(f'{FAIL}Valor digitado deve ser inteiro, tente novamente{ENDC}')
        

    if escolha_dificuldade == 1:
        dificuldade = easy.copy()
        dificuldade_name = 'easy'
    elif escolha_dificuldade == 2:
        dificuldade = medium.copy()
        dificuldade_name = 'medium'
    elif escolha_dificuldade == 3:
        dificuldade = medium.copy()
        dificuldade_name = 'hard'
    elif escolha_dificuldade == 4:
        dificuldade = english.copy()
        dificuldade_name = 'english'

    return dificuldade, dificuldade_name

def regras(dificuldade_name):
    if dificuldade_name == 'english':
        sys('cls')
        print(f'\t\t{HEADER}{BOLD}THE RULES OF HANGMAN:\n{ENDC}')
        print(f'{BOLD}\tA RANDOM WORD WILL BE SELECTED, AND FOR EACTH LETTER WILL BE DRAWN A LINE ({FAIL} _ {ENDC}{BOLD})')
        print(f'\tTHE PLAYER WILL GUESS ONE LETTER AT A TIME, AND IF THIS {OKGREEN}LETTER IS IN THE WORD IT WILL APPEAR IN POSITION{ENDC}{BOLD}\n\tIF THE PLAYER {FAIL}MISS THE LETTER 1 LIFE WILL BE TAKEN AWAY{ENDC}{BOLD}')
        print(f'\tWHEN {FAIL}ALL 6 LIFES IS LOST THE GAME WILL END{ENDC}{BOLD}')
        print(f'\t{OKGREEN}IF THE PLAYER GUESS ALL THE LETTERS IN THE WORD, THE NEXT WORD WILL BE SELECTED, AND THE LIFES WILL BE RESET{ENDC}')
        print(f'\n\t{BOLD}YOU CAN GUESS LETTER BY LETTER OR TRY TO GUESS THE WHOLE WORD, IF WRONG, THE SAME AMOUT OF LIFES WILL BE LOST')
        print(f'\tTRY TO CORRECTLY GUESS EVERY WORD IN EVERY LEVEL, AND YOU WILL BE A TRULLY WORD MASTER{ENDC}')
        print(f'\n\n{WARNING}--->PRESS ANY KEY TO GO BACK TO MAIN MENU<---\n')
        sair = input(f'--->{ENDC}')

    else:
        sys('cls')
        print(f'\t\t{HEADER}{BOLD}REGRAS DO JOGO DA FORCA:\n{ENDC}')
        print(f'\t{BOLD}UMA PALAVRA ALEATÓRIA VAI SER ESCOLHIDA E PARA CADA LETRA VAI SER DESENHADA UMA LINHA ({FAIL} _ {ENDC}{BOLD})')
        print(f'\tO JOGADOR IRA ADIVINHAR UMA LETRA POR VEZ, E SE {OKGREEN}CORRETO A LETRA IRÁ APARECER NO LUGAR ADEQUADO{ENDC}{BOLD}\n\tSE O JOGADOR {FAIL}ERRAR A LETRA 1 VIDA SERA PERDIDA{ENDC}{BOLD}')
        print(f'\tQUANDO {FAIL}TODAS AS 6 VIDAS FOREM PERDIDAS O JOGO IRÁ ACABAR{ENDC}{ENDC}')
        print(f'\t{OKGREEN}SE O JOGADOR ADIVINHAR TODAS AS LETRAS DA PALAVRA, UMA PRÓXIMA PALAVRA SERA ESCOLHIDA, E AS VIDAS SERÃO RESETADAS{ENDC}')
        print(f'\n\tVOCE PODE ADIVINHAR LETRA POR LETRA OU TENTAR ADIVINHAR A PALAVRA INTEIRA, SE ERRAR A MESMA QUANTIDADE DE VIDAS SERÁ PERDIDA')
        print(f'\tTENTE ACERTAR TODAS AS PALAVRAS DE TODOS OS NÍVEIS, E VOCÊ SERÁ UM VERDADEIRO MESTRE DAS PALAVARS{ENDC}')
        print(f'\n\n{WARNING}--->PRESSIONE QUALQUER TECLA PARA VOLTAR AO MENU PRINCIPAL<---\n')
        sair = input(f'--->{ENDC}')

def ranking(ranking_list, dificuldade_name):
    easy_list = []
    medium_list = []
    hard_list = []
    english_list = []
    for person in ranking_list:
        _, level, _ = person
        if level == 'easy':
            easy_list.append(person)
        elif level == 'medium':
            medium_list.append(person)
        elif level == 'hard':
            hard_list.append(person)
        elif level == 'english':
            english_list.append(person)

    easy_list.sort(key=lambda tupla: tupla[2], reverse=True)
    medium_list.sort(key=lambda tupla: tupla[2], reverse=True)
    hard_list.sort(key=lambda tupla: tupla[2], reverse=True)
    english_list.sort(key=lambda tupla: tupla[2], reverse=True)

    easy_list = easy_list[:10]
    medium_list = medium_list[:10]
    hard_list = hard_list[:10]
    english_list = english_list[:10]

    if dificuldade_name == 'english':
        sys('cls')
        while True:
            try:
                print(f'\t\t{HEADER}{BOLD}RANKINGS{ENDC}\n\n\t{BOLD}[1] EASY\n\t[2] MEDIUM\n\t[3] HARD\n\t[4] ENGLISH\n\n\t{OKGREEN}[5] MAIN MENU\n{ENDC}')
                escolha_ranking = int(input(f'{WARNING}--->{ENDC}'))
                break
            except ValueError:
                sys('cls')
                print(f'{FAIL}typed input must be integer, try again{ENDC}')
    else:
        sys('cls')
        while True:
            try:
                print(f'\t\t{HEADER}{BOLD}RANKINGS{ENDC}\n\n\t{BOLD}[1] EASY\n\t[2] MEDIUM\n\t[3] HARD\n\t[4] ENGLISH\n\n\t{OKGREEN}[5] MENU PRINCIPAL\n{ENDC}')
                escolha_ranking = int(input(f'{WARNING}--->{ENDC}'))
                break
            except ValueError:
                sys('cls')
                print(f'{FAIL}Valor digitado deve ser inteiro, tente novamente{ENDC}')
    
    if escolha_ranking == 1:
        sys('cls')
        print(f'\t\t\t{HEADER}{BOLD}EASY RANKINGS{ENDC}')
        for i in easy_list:
            nome, _, fase = i
            print(f'\t{BOLD}{nome} ---> {OKGREEN}{fase}{ENDC}')

        if dificuldade_name == 'english':
            print(f'\n\n{WARNING}--->PRESS ANY KEY TO GO BACK TO MAIN MENU<---\n{ENDC}')
        else:
            print(f'{WARNING}\n\n--->PRESSIONE QULQUER TECLA PARA VOLTAR AO MENU PRINCIPAL<---\n{ENDC}')
        sair = input(f'{WARNING}--->{ENDC}')

    elif escolha_ranking == 2:
        sys('cls')
        print(f'\t\t\t{HEADER}{BOLD}MEDIUM RANKINGS{ENDC}')
        for i in medium_list:
            nome, _, fase = i
            print(f'\t{BOLD}{nome} ---> {OKGREEN}{fase}{ENDC}')

        if dificuldade_name == 'english':
            print(f'\n\n{WARNING}--->PRESS ANY KEY TO GO BACK TO MAIN MENU<---\n{ENDC}')
        else:
            print(f'\n\n{WARNING}--->PRESSIONE QULQUER TECLA PARA VOLTAR AO MENU PRINCIPAL<---\n{ENDC}')
        sair = input(f'{WARNING}--->{ENDC}')

    elif escolha_ranking == 3:
        sys('cls')
        print(f'\t\t\t{HEADER}{BOLD}HARD RANKINGS{ENDC}')
        for i in hard_list:
            nome, _, fase = i
            print(f'\t{BOLD}{nome} ---> {OKGREEN}{fase}{ENDC}')

        if dificuldade_name == 'english':
            print(f'{WARNING}\n\n--->PRESS ANY KEY TO GO BACK TO MAIN MENU<---\n{ENDC}')
        else:
            print(f'{WARNING}\n\n--->PRESSIONE QULQUER TECLA PARA VOLTAR AO MENU PRINCIPAL<---\n{ENDC}')
            sair = input(f'{WARNING}--->{ENDC}')

    elif escolha_ranking == 4:
        sys('cls')
        print(f'\t\t\t{HEADER}{BOLD}ENGLISH RANKINGS{ENDC}')
        for i in english_list:
            nome, _, fase = i
            print(f'\t{BOLD}{nome} ---> {OKGREEN}{fase}{ENDC}')

        if dificuldade_name == 'english':
            print(f'{WARNING}\n\n--->PRESS ANY KEY TO GO BACK TO MAIN MENU<---\n{ENDC}')
        else:
            print(f'{WARNING}\n\n--->PRESSIONE QULQUER TECLA PARA VOLTAR AO MENU PRINCIPAL<---\n{ENDC}')
        sair = input(f'{WARNING}--->{ENDC}')

    return 1

