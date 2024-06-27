import math
from math import trunc

exercicio = ' Exercício 016 '
enunciado = 'Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. \n' \
            'Ex: Digite um número: 6.127. O número 6.127 tem a parte Inteira 6.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

numReal = float(input('Digite um número Real: '))
print(f'O número {numReal} tem a parte Inteira {math.trunc(numReal)}.')
print(f'O número {numReal} tem a parte Inteira {int(numReal)}.')
print(f'O número {numReal} tem a parte Inteira {numReal:.0f}.')

