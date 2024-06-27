exercicio = ' Exercício 070 '
enunciado = """Crie um programa que leia o nome e o preço de vários produtos. O programa deverá 
perguntar se o usuário vai continuar. No final, mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$1000.
c) Qual é o nome do produto mais barato."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')
print('-'*40)
print(f'{"LOJA SUPER BARATÃO":^40}')
print('-'*40)
totalcompra = maisdemil = precomaisbarato = contador = 0
nomemaisbarato = ''
while True:
    nomeproduto = str(input('Nome do Produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    totalcompra += preco
    contador += 1
    if preco > 1000:
        maisdemil += 1
    if contador == 1 or preco < precomaisbarato:
        nomemaisbarato = nomeproduto
        precomaisbarato = preco
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'{"FIM DO PROGRAMA":-^40}')
print(f'O total da compra foi R${totalcompra}')
print(f'Temos {maisdemil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {nomemaisbarato} que custa R${precomaisbarato:.2f}')

