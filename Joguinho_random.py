#Joguinho do "Consegue adivinhar"
'''
    Autor: Victilson Victor Fortes
    Aprendendo Python
'''
#Aqui vamos importar as nossa libs
import random
from time import sleep #importei a função sleep da lib time
from os import system
import emoji #Vamos trabalhar com emojis

#Definindo um cabeçalho para o jogo
def game_head():
    print('\t\t\t\tCONSEGUE ADIVINHAR?\n\n\n')

#Cabeçalho do game
game_head()

#Guardei a mensagem de boas vinda numa variavel para poder usar a função sleep
welcome_msg = 'Seja bem-vindo(a) ao joguinho\n\t\t\t\tPressione ENTER'
for wait in welcome_msg:
    print(wait, end='', flush=True)
    sleep(.2)
input()

#Vamos limpar a tela
system("cls")

#Cabeçalho do game
game_head()

explain_msg = 'O jogo consiste no seguinte: Eu vou pensar em um número e você tenta adivinhá-lo\n\t\t\t\tPRESSIONE ENTER' 
for wait in explain_msg:
    print(wait,end='',flush=True)
    sleep(.1)
input()

#Vamos limpar a tela
system("cls")

#Cabeçalho do game
game_head()


print('Cá vai uma dica: Eu vou pensar apenas em números inteiros e positivos de 1 à 5\nEntão vamos começar o jogo\n\t\t\t\tPRESSIONE ENTER')
input()

#Vamos apagar a tela
system('cls')

while True: #Enquanto o usuário pretender jogar o programa vai começar desse ponto

    #Cabeçalho do game
    game_head()

    number = random.randint(1,5)

    print('____________________')
    _try=int(input('\n\n\n\t\tEm que número estou a pensar:'))
    

    #Vamos avaliar as tentaivas inválidas
    if _try <=0 or _try >5:
        print(emoji.emojize("Não acertavas nem em sombras:sleepy:\n",use_aliases= True))
        system('cls')
    
    else:

        if _try == number:
            print(emoji.emojize('\n\n\t\t\t\tParabéns você acertou :smile:\nVocê é tão incrível:hushed: ...Até parece que leu minha memória :sweat_smile:\n',use_aliases=True))
        else:
            print(emoji.emojize('\n\t\t\t\thahahah Eu venci,tenta na próxima:yum:',use_aliases=True))

        game_continue = input('Quer jogar novamente?(s/n)\n')
        system("cls")
        
        #CAso o usuario não quiser mais jogar
        if game_continue == 'N' or game_continue == 'n':
            print('saindo...\n')
            sleep(2.8)
            break

        #Se quiser continuar
        elif game_continue =='S' or game_continue=='s':
            print('Pensando em outro número..')
            sleep(1.4)
            system('cls')


system('pause')
