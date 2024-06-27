exercício = ' Exercício 013 '
enunciado = 'Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'
fim = '='*30
print(f'{exercício:=^30} \n{enunciado} \n{fim}')

sal = float(input("Digite o salário do funcionário: R$ "))
aum = 15
nvsal = sal + (aum/100*sal)

print(f"O novo salário do funcionário com aumento de 15% será R$ {nvsal:.2f}")
