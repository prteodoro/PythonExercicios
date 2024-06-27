exercicio = ' Exercício 071 '
enunciado = """Crie um programa que simule o funcionamento de um caixa eletrônico. No início, 
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar 
quantas cédulas de cada valor serão entregues.
OBS.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

print('='*40)
print(f'{"Banco CEV":^40}')
print('='*40)
saque = int(input('Que valor você quer sacar? R$'))
while True:
    if saque // 50 >= 1:
        cedulasde50 = saque // 50
        saque = saque % 50
        print(f'Total de {cedulasde50} cédulas de R$50.00')
    elif saque // 20 >= 1:
        cedulasde20 = saque // 20
        saque = saque % 20
        print(f'Total de {cedulasde20} cédulas de R$20.00')
    elif saque // 10 >= 1:
        cedulasde10 = saque // 10
        saque = saque % 10
        print(f'Total de {cedulasde10} cédulas de R$10.00')
    elif saque // 1 >= 1:
        cedulasde1 = saque // 1
        saque = saque % 1
        print(f'Total de {cedulasde1} cédulas de R$1.00')
    if saque == 0:
        break
print('='*40)
print(f'Volte sempre ao BANCO CEV! Tenha um bom dia!')
