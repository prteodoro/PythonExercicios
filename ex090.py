exercicio = ' Exercício 090 '
enunciado = """Faça um programa que leia nome e média de um aluno, guardando também a situação 
em um dicionário. No final, mostre o conteúdo da estrutura na tela."""
fim = '='*50
print(f'{exercicio:^50} \n{enunciado} \n{fim}')

aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
elif aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Aprovado'
print('-='*25)

for k, v in aluno.items():
    print(f'- {k} é igual a {v}.')
