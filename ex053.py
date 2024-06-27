exercicio = ' Exercício 053 '
enunciado = """Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando 
os espaços. (Palíndromos são palavras/frases que podem ser lidas de frente para trás ou de trás para 
frente que formam as mesmas palavras/frases.
Ex: apos a sopa"""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

frase = str(input('Digite uma frase: ')).upper().replace(" ", "")
inverso = ''
for c in range(len(frase) - 1, -1, -1):
    inverso += frase[c]
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

print('\nSOLUÇÃO SEM FOR')
inverso02 = frase[::-1]
print(f'O inverso de {frase} é {inverso02}')
