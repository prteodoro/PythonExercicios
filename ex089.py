from time import sleep

exercicio = ' Exercício 089 '
enunciado = """Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em 
uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o 
usuário possa mostrar as notas de cada aluno individualmente."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

lista = []
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota01 = float(input('Nota 01: '))
    nota02 = float(input('Nota 02: '))
    media = (nota01 + nota02) / 2
    lista.append([nome, [nota01, nota02], media])
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-='*20)
print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-'*25)
for pos, aluno in enumerate(lista):
    print(f'{pos + 1:<4} {aluno[0]:<10} {aluno[2]:>8.1f}')
print('-'*25)
while True:
    codigoaluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if codigoaluno == 999:
        print(f'FINALIZANDO...')
        break
    print(f'Notas de {lista[codigoaluno - 1][0]} são {lista[codigoaluno - 1][1]}')
    print('-' * 35)
sleep(2)
print('<<< VOLTE SEMPRE >>>')
