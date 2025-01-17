exercicio = ' Exercício 084 '
enunciado = """Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em 
uma lista. No final, mostre:
	A) Quantas pessoas foram cadastradas.
	B) Uma listagem com as pessoas mais pesadas.
	C) Uma listagem com as pessoas mais leves."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

pessoas = []
dados = []
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        menorpeso = dados[1]
        maiorpeso = dados[1]
    else:
        if dados[1] < menorpeso:
            menorpeso = dados[1]
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-='*25)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorpeso}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menorpeso}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end=' ')
