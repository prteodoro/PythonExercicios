from datetime import date

exercicio = ' Exercício 092 '
enunciado = """Crie um programa que leia nome, ano de nascimento, e carteira de trabalho e 
cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o 
dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da 
idade, com quantos anos a pessoa vai se aposentar."""
fim = '='*50
print(f'{exercicio:^50} \n{enunciado} \n{fim}')

pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
anonascimento = int(input('Ano de Nascimento: '))
pessoa['Idade'] = date.today().year - anonascimento
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CTPS'] > 0:
    pessoa['Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Contratação'] + 35 - anonascimento
print('-='*30)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')