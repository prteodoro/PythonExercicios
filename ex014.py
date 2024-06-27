exercicio = ' Exercício 014 '
enunciado = 'Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

tempC = float(input('Digite uma temperatura ºC: '))
tempF = (tempC * 9/5) + 32
print(f'A temperatura de {tempC:.0f}ºC é equivalente a {tempF:.0f}ºF.')
