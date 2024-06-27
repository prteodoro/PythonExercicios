exercicio = ' Exercício 030 '
enunciado = 'Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

num = int(input('Me diga um número qualquer: '))
if num % 2 == 0:
    print(f'O número {num} é PAR.')
else:
    print(f'O número {num} é ÍMPAR.')
