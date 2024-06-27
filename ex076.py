exercicio = ' Exercício 076 '
enunciado =  """Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos 
preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

produtos = (str(input('Produto: ')).strip().capitalize(), float(input('Preço: ')),
            str(input('Produto: ')).strip().capitalize(), float(input('Preço: ')),
            str(input('Produto: ')).strip().capitalize(), float(input('Preço: ')))
print('-'*48)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*48)
total = 0
for posicao in produtos:
    if produtos.index(posicao) % 2 == 0:
        print(f'{posicao:.<40}', end='')
    else:
        print(f'R${posicao:>6.2f}')
        total += posicao
print('-'*48)
print(f'{"TOTAL":<40}R${total:>6.2f}')
print('-'*48)
