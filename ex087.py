exercicio = ' Exercício 087 '
enunciado = """Aprimore o desafio anterior, mostrando no final:
	A) A soma de todos os valores pares digitados.
	B) A soma dos valores da terceira coluna.
	C) O maior valor da segunda linha."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

valores = [[], [], []]
somapares = somacoluna3 = maiorlinha2 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        valores[linha].append(num)
        #if num % 2 == 0:
        #    somapares += num
        #if coluna == 2:
        #    somacoluna3 += num
        #if linha == 1 and coluna == 0:
        #    maiorlinha2 = num
        #elif linha == 1 and num > maiorlinha2:
        #    maiorlinha2 = num
print('-='*25)
for valor in valores:
    for pos in range(0, 3):
        print(f'[{valor[pos]:^5}]', end=' ')
    print()
print('-='*25)
for linha in range(0, 3):
    for coluna in range(0, 3):
        if valores[linha][coluna] % 2 == 0:
            somapares += valores[linha][coluna]
print(f'A soma dos valores pares é {somapares}.')
for linha in range(0,3):
    somacoluna3 += valores[linha][2]
print(f'A soma dos valores da terceira coluna é {somacoluna3}.')
for pos in range(0, 3):
    if pos == 0:
        maiorlinha2 = valores[1][pos]
    elif valores[1][pos] > maiorlinha2:
        maiorlinha2 = valores[1][pos]
#print({max(valores[1])})  Solução usando a função max
print(f'O maior valor da segunda linha é {maiorlinha2}.')
