exercicio = ' Exercício 086 '
enunciado = """Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

matriz = [[], [], []]
for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha].append(num)
print('-='*25)
for valor in matriz:
    for pos in range(0, 3):
        print(f'[{valor[pos]:^5}]', end='')
    print()
