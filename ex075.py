exercicio = ' Exercício 075 '
enunciado = """Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
No final, mostre:
	A) Quantas vezes apareceu o valor 9.
	B) Em que posição foi digitado o primeiro valor 3.
	C) Quais foram os números pares."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

numeros = (int(input('Digite o último número: ')), int(input('Digite o último número: ')),
           int(input('Digite o último número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
tempar = 0
for cont in range(0, len(numeros)):
    if numeros[cont] % 2 == 0:
        tempar += 1
        if tempar == 1:
            print(f'Os valores pares digitados foram ', end='')
        print(numeros[cont], end=' ')
if tempar == 0:
    print(f'Não foram digitados valores pares')
    