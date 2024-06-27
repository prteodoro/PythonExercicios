from time import sleep
from random import choice
import emoji

exercicio = ' Exercício 045 '
enunciado = 'Crie um programa que faça o computador jogar Jokenpô com você.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')
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
if jogador == 0:
    jogador = 'PEDRA'
elif jogador == 1:
    jogador = 'PAPEL'
elif jogador == 2:
    jogador = 'TESOURA'
else:
    print('OPÇÃO INVÁLIDA. Tente novamente!')
computador = choice(['PEDRA', 'PAPEL', 'TESOURA'])
wincomputador = 'O COMPUTADOR VENCEU!!!'
winjogador = 'PARABÉNS, VOCÊ VENCEU!!!'
if computador == jogador:
    resultado = 'EMPATE!'
elif computador == 'PEDRA' and jogador == 'PAPEL':
    resultado = winjogador
elif computador == 'PEDRA' and jogador == 'TESOURA':
    resultado = wincomputador
elif computador == 'PAPEL' and jogador == 'PEDRA':
    resultado = wincomputador
elif computador == 'PAPEL' and jogador == 'TESOURA':
    resultado = winjogador
elif computador == 'TESOURA' and jogador == 'PEDRA':
    resultado = winjogador
elif computador == 'TESOURA' and jogador == 'PAPEL':
    resultado = wincomputador
else:
    resultado = 'OPÇÃO INVÁLIDA. Tente novamente!'
design = '-='*15
print(f"""{design}
Computador jogou {computador}
Jogador jogou {jogador}
{design}""")
print(resultado)
