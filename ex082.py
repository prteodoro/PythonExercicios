exercicio = ' Exercício 082 '
enunciado = """Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os 
valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

valores = []
pares = []
impares = []
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-='*25)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
