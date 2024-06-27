from time import sleep

exercício = ' Exercício 047 '
enunciado = 'Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'
fim = '='*30
print(f'{exercício:=^30} \n{enunciado} \n{fim}')

for numerospares in range(2, 51, 2):
    print(numerospares, end=' ')
    sleep(0.3)
print('ACABOU!')
