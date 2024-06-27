from random import randint
from time import sleep

exercício = ' Exercício 028 '
enunciado = """Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça 
para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever 
na tela se o usuário venceu ou perdeu."""
fim = '='*30
print(f'{exercício:=^30} \n{enunciado} \n{fim}')

print('-=-'*17)
print(f'Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-'*17)
num = int(input('Em que número eu pensei? '))
numpc = randint(0, 5)
print(f'PROCESSANDO...')
sleep(3)
if num == numpc:
    print(f'PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {numpc} e não no {num}!')




