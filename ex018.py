from math import radians, sin, cos, tan

exercicio = 'Exercício 018 '
enunciado = 'Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente \n' \
            'desse ângulo.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}.')
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}.')
print(f'O ângulo de {angulo} tem o TANGENTE de {tangente:.2f}.')
