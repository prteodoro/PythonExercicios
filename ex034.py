exercicio = ' Exercício 034 '
enunciado = """Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%."""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

salario = float(input('Qual é o salário do funcionário? '))
if salario > 1250:
    novosalario = salario + (salario * 10 / 100)
else:
    novosalario = salario + (salario * 15 / 100)
print(f'Quem ganhava R${salario} passa a ganhar R${novosalario:.2f} agora.')
