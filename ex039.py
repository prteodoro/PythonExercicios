from datetime import date

exercicio = ' Exercício 040 '
enunciado = """Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
	- Se ele ainda vai se alistar ao serviço militar.
	- Se é a hora de se alistar.
	- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

anonascimento = int(input('Ano de nascimento: '))
idade = date.today().year - anonascimento
idadealistamento = 18
print(f'Quem nasceu em {anonascimento} tem {idade} anos em {date.today().year}.')
if idade < idadealistamento:
    print(f"""Ainda falta(m) {idadealistamento - idade} ano(s) para o alistamento
Seu alistamento será em {anonascimento + idadealistamento}.""")
elif idade > idadealistamento:
    print(f"""Você já deveria ter se alistado há {idade - idadealistamento} ano(s).
Seu alistamento foi em {anonascimento + idadealistamento}.""")
else:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
