exercicio = ' Exercício 078 '
enunciado = """Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-'*40)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições', end=' ')
for posicao, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{posicao}...', end=' ')
print(f'\nO menor valor digitado foi {min(valores)} nas posições', end=' ')
for posicao, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{posicao}...', end=' ')
