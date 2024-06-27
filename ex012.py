exercicio = ' Exercício 012 '
enunciado = 'Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

preco = float(input('Digite o preço do produto: R$ '))
desc = 5
nvpreco = preco - (desc/100*preco)

print(f'O valor desse produto com 5% de desconto é R$ {nvpreco:.2f}')
