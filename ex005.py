exercicio = ' Exercício 005 '
enunciado = 'Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

n = int(input(f'Digite um número: '))
ant = n - 1
suc = n + 1
print(f'\nO antecessor de {n} é {ant} e o seu sucessor é {suc}.')
#print(f'\nO antecessor de {n} é {n-1} e o seu sucessor é {n+1}.')






