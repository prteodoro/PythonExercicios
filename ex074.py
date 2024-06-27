from random import choice, randint

exercicio = ' Exercício 074 '
enunciado = """Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor 
que estão na tupla."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')
sorteados = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteei os valores {sorteados}')
print(f'\nO maior valor sorteado foi {max(sorteados)}')
print(f'O menor valor sorteado foi {min(sorteados)}')



