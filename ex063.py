exercicio = ' Exercício 063 '
enunciado = """Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros 
elementos de uma Sequência de Fibonacci. 
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8"""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')
print('-'*40)
print(f'Sequência de Fibonacci')
print('-'*40)
quantostermos = int(input('Quantos termos você quer mostrar? '))
print('~'*40)
contador = 0
termoa = 0
termob = 1
while contador < quantostermos:
    print(termoa, '→ ', end='')
    termoa = termob - termoa
    termob = termob + termoa
    contador += 1
print('FIM')
print('~'*40)
