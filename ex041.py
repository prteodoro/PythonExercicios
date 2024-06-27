from datetime import date

exercicio = ' Exercício 041 '
enunciado = """A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de 
um atleta e mostre sua categoria, de acordo com a idade:
	- Até 09 anos: MIRIM
	- Até 14 anos: INFANTIL
	- Até 19 anos: JUNIOR
	- Até 25 anos: SÊNIOR
	- Acima: MASTER"""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

anonascimento = int(input('Ano de Nascimento: '))
idade = date.today().year - anonascimento
print(f'O atleta tem {idade} ano(s).')
if idade <= 9:
    categoria = 'MIRIM'
elif idade > 9 and idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print(f'Classificação: {categoria}')
