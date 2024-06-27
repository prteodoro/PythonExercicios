exercicio = ' Exercício 069 '
enunciado = """069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa 
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final. mostre:
a) Quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

maisde18 = totalhomens = mulheresmenosde20 = 0
while True:
    print('-'*40)
    print('CADASTRE UMA PESSOA')
    print('-' * 40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 40)
    resposta = ' '
    if idade >= 18:
        maisde18 += 1
    if sexo == 'M':
        totalhomens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenosde20 += 1
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-' * 40)
print(f'Total de pessoas com mais de 18 anos: {maisde18}')
print(f'Ao todo temos {totalhomens} homen(s) cadastrado(s).')
print(f'E temos {mulheresmenosde20} mulher(es) com menos de 20 anos.')
