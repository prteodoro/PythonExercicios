exercicio = ' Exercício 015 '
enunciado = 'Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade \n' \
            'de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 \n' \
            'por dia e R$ 0,15 por Km rodado.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R$ {total:.2f}.')

