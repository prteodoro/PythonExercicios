exercicio = ' Exercício 008 '
enunciado = 'Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

metro = float(input('Quantos metros deseja converter? '))
cent = metro * 100
milim = metro * 1000

print(f'{metro} metro(s) em centímetros é equivalente a {cent:.0f} centímetros.')
print(f'{metro} metro(s) em milímetros é equivalente a {milim:.0f} milímetros.')
