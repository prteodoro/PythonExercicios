exercício = ' Exercício 029 '
enunciado = """Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite."""
fim = '='*30
print(f'{exercício:=^30} \n{enunciado} \n{fim}')

velocidadeatual = float(input('Qual é a velocidade atual do carro? '))

if velocidadeatual > 80:
    valormulta = (velocidadeatual - 80) * 7
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h \n'
          f'Você deve pagar uma multa de R${valormulta:.2f}!')
print(f'Tenha um BOM DIA! Dirija com segurança!')
