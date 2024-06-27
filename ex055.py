exercicio = ' Exercício 055 '
enunciado = """Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o 
menor peso lidos."""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: Kg '))
    if c == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print(f'O maior peso lido foi de {maiorpeso}Kg')
print(f'O menor peso lido foi de {menorpeso}Kg')
