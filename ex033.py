exercicio = ' Exercício 033 '
enunciado = 'Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

valor01 = int(input('Primeiro valor: '))
valor02 = int(input('Segundo valor: '))
valor03 = int(input('Terceiro valor: '))

menorvalor = valor01

if valor02 < valor01 and valor02 < valor03:
    menorvalor = valor02
if valor03 < valor01 and valor03 < valor02:
    menorvalor = valor03
print(f'O menor valor digitado foi {menorvalor}.')

maiorvalor = valor01
if valor02 > maiorvalor:
    maiorvalor = valor02
if valor03 > maiorvalor:
        maiorvalor = valor03
print(f'O maior valor digitado foi {maiorvalor}')
