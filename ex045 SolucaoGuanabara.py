from time import sleep
from random import randint
import emoji

exercicio = ' Exercício 045 '
enunciado = 'Crie um programa que faça o computador jogar Jokenpô com você.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print(f"""Suas opções:
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*15)
print(f'O Computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-='*15)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
else:
    print('JOGADA INVÁLIDA')
