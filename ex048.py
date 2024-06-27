exercicio = ' Exercício 048 '
enunciado = """Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos 
de três e que se encontram no intervalo de 1 até 500."""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

qtd = 0
soma = 0
for multiplode3 in range(3, 501, 3):
    if multiplode3 % 2 != 0:
        qtd += 1
        soma += multiplode3
        print(multiplode3, end=' ')
print(f'\nA soma de todos os {qtd} valores é {soma}')

