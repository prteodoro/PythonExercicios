from random import choice

exercicio = ' Exercício 019 '
enunciado = 'Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que \n' \
            'ajude ele, lendo o nome deles e escrevendo o nome do escolhido.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

aluno01 = input('Digite o nome do primeiro aluno: ')
aluno02 = input('Digite o nome do segundo aluno: ')
aluno03 = input('Digite o nome do terceiro aluno: ')
aluno04 = input('Digite o nome do quarto aluno: ')
lista = [aluno01, aluno02, aluno03, aluno04]
alunoescolhido = choice(lista)

print(f'O aluno escolhido foi {alunoescolhido}.')
