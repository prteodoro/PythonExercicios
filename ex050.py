exercicio = ' Exercício 050 '
enunciado = """Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles 
que forem pares. Se o valor digitado for ímpar, desconsidere-o."""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

soma = 0
qtd = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        qtd += 1
        soma += num
print(f'Você digitou {qtd} números pares, e a soma dos números pares digitados é {soma}.')
