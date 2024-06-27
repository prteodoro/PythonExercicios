exercicio = ' Exercício 038 '
enunciado = """038 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na 
tela uma mensagem:
	- O primeiro valor é maior
	- O segundo valor é maior
	- Não existe valor maior, os dois são iguais"""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

num01 = int(input('Primeiro número: '))
num02 = int(input('Segundo número: '))
if num01 > num02:
    print('O PRIMEIRO valor é maior.')
elif num02 > num01:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS.')
