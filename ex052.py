exercicio = ' Exercício 052 '
enunciado = 'Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

num = int(input('Digite um número: '))
qtdxdivisivel = 0
for c in range(1, num + 1):
    if num % c == 0:
        qtdxdivisivel += 1
        print(f'\033[33m{c}\033[m', end=' ')
    else:
        print(f'\033[31m{c}\033[m', end=' ')
print(f'\nO número {num} foi divisível {qtdxdivisivel} vezes')
if qtdxdivisivel == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
