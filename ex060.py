exercicio = ' Exercício 060 '
enunciado = """Faça um programa que leia um número qualquer e mostre o seu fatorial. 
Ex: 5! = 5x4x3x2x1 = 120"""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

num = int(input('Digite um número \npara calcular seu fatorial: '))
print(f'Calculando {num}! = ', end='')
fatorial = 1
contador = num
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(fatorial)
