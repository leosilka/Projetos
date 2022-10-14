import random
import time
cores = {'limpa': '\033[m',
         'preto': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m',}
print('\033[1;32m===============================\033[m')
print('\033[1;35mPROJETO 01 - ADIVINHE O NÚMERO\033[m')
print('\033[1;32m===============================\033[m')
print('Olá, seja bem vindo ao jogo de adivinhe o número que estou pensando.\nNeste jogo, você deverá adivinhar um número e eu irei lhe informar \nse esta correto ou errado. Sem mais delongas, vamos começar!')
print('-'*31)
print('')
nome = str(input('Caro Player, gostariamos antes de começar, saber o seu nome: ')).strip()
print('================================')
print('Menu Interativo')
print('{}[ 1 ]{} Para jogar com 5 números {}(fácil){}' .format(cores['amarelo'], cores['limpa'], cores['amarelo'], cores['limpa']))
print('{}[ 2 ]{} Para jogar com 10 números {}(médio){}' .format(cores['azul'], cores['limpa'], cores['azul'], cores['limpa']))
print('{}[ 3 ]{} Para jogar com 20 números {}(díficil){}' .format(cores['cinza'], cores['limpa'], cores['cinza'], cores['limpa']))
print('{}[ 4 ]{} Para jogar com 50 números {}(mestre){}' .format(cores['preto'], cores['limpa'], cores['preto'], cores['limpa']))
print('================================')
escolha = int(input('Escolha uma opção de jogo: '))
cont = 0
acertos = 0
erros = 0
if escolha == 1:
    for c in range(1, 6):
        nsort = random.randint(0, 5)
        nesco = int(input('{}, escolha um número entre 0 e 5: ' .format(nome)))
        print('Processando...')
        time.sleep(2)
        if nesco == nsort:
            print('Parabéns {}, você acertou um número.' .format(nome))
            acertos += 1
        else:
            print('{}. Infelizmente você errou!' .format(nome))
            print('O número que eu escolhi foi {}' .format(nsort))
            erros += 1
        cont += 1
        print('-'*15)
if escolha == 2:
    for c in range(1, 6):
        nsort = random.randint(0, 10)
        nesco = int(input('{}, escolha um número entre 0 e 10: ' .format(nome)))
        print('Processando...')
        time.sleep(2)
        if nesco == nsort:
            print('Parabéns {}, você acertou um número.' .format(nome))
            acertos += 1
        else:
            print('{}. Infelizmente você errou!' .format(nome))
            print('O número que eu escolhi foi {}' .format(nsort))
            erros += 1
        cont += 1
        print('-'*15)
if escolha == 3:
    for c in range(1, 6):
        nsort = random.randint(0, 20)
        nesco = int(input('{}, escolha um número entre 0 e 20: ' .format(nome)))
        print('Processando...')
        time.sleep(2)
        if nesco == nsort:
            print('Parabéns {}, você acertou um número.' .format(nome))
            acertos += 1
        else:
            print('{}. Infelizmente você errou!' .format(nome))
            print('O número que eu escolhi foi {}' .format(nsort))
            erros += 1
        cont += 1
        print('-'*15)
if escolha == 4:
    for c in range(1, 6):
        nsort = random.randint(0, 50)
        nesco = int(input('{}, escolha um número entre 0 e 50: ' .format(nome)))
        print('Processando...')
        time.sleep(2)
        if nesco == nsort:
            print('Parabéns {}, você acertou um número.' .format(nome))
            acertos += 1
        else:
            print('{}. Infelizmente você errou!' .format(nome))
            print('O número que eu escolhi foi {}' .format(nsort))
            erros += 1
        cont += 1
        print('-'*15)
print('{}, você obteve um total de {} acertos e {} erros' .format(nome, acertos, erros))
