from random import sample, shuffle

exercicio = " Exercício 020 "
enunciado = 'O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. \n' \
            'Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

aluno01 = input('Primeiro aluno: ')
aluno02 = input('Segundo aluno: ')
aluno03 = input('Terceiro aluno: ')
aluno04 = input('Quarto aluno: ')
lista = [aluno01, aluno02, aluno03, aluno04]

# Usando a função sample
print(f'A ordem de apresentação será {sample(lista, k=len(lista))}')

# Usando a função shuffle
shuffle(lista)
print(f'A ordem de apresentação será {lista}')


