exercicio = ' Exercício 010 '
enunciado = 'Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ' \
            'ela pode comprar. Considere US$ 1,00 = R$ 3,27'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

real = float(input(f'Digite quantos R$ você deseja converter: R$ '))
dolar = real / 3.27

print(f'Com R$ {real:.2f} você pode comprar US$ {dolar:.2f}')
print(fim)

