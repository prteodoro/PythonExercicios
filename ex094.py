exercicio = ' Exercício 094 '
enunciado = """Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados 
de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
	A) Quantas pessoas foram cadastradas
	B) A média de idade do grupo
	C) Uma lista com todas as mulheres
	D) Uma lista com todas as pessoas com idade acima da média"""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

pessoa = {}
lista = []
somaidade = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while pessoa['sexo'] not in 'MF':
        print(f'ERRO! Responda apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    lista.append(pessoa.copy())
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resposta not in 'SN':
        print(f'ERRO! Responda apenas S ou N.')
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break
print('-='*30)
print(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = somaidade / len(lista)
print(f'B) A média de idade é de {media:.0f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média:')
for p in lista:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'  {k} = {v};', end=' ')
        print()
print(f'<< ENCERRADO >>')
