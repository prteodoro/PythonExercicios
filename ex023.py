exercicio = ' Exercício 023 '
enunciado = """Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados: 
Ex.: Digite um número: 1834  unidade: 4 dezena: 3 centena: 8 milhar: 1"""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

num = str(input(f'Digite um número: '))
print(f'Unidade: {num.zfill(4)[3]}')
print(f'Dezena: {num.zfill(4)[2]}')
print(f'Centena: {num.zfill(4)[1]}')
print(f'Milhar: {num.zfill(4)[0]}')

print(f'\nSolução usando int')
num = int(input('Informe um número: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')









