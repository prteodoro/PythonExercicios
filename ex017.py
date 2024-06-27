from math import hypot

exercicio = ' Exercício 017 '
enunciado = 'Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo \n' \
            'retângulo, calcule e mostre o comprimento da hipotenusa.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

catetoOposto = float(input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = hypot(catetoOposto, catetoAdjacente)
print(f'O comprimento da hipotenusa é de {hipotenusa:.2f}.')


