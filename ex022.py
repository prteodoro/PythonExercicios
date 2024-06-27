exercicio = ' Exercício 022 '
enunciado = """Crie um programa que leia o nome completo de uma pessoa e mostre:
    O nome com todas as letras maiúsculas
	O nome com todas minúsculas
	Quantas letras ao todo (sem considerar espaços)
	Quantas letras tem o primeiro nome."""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

nomecompleto = str(input('Digite um nome completo: '))
print(f'Nome em letras maiúsculas: {nomecompleto.upper()}')
print(f'Nome em letras minúsculas: {nomecompleto.lower()}')
print(f'Total de letras sem espaços: {len(nomecompleto.replace(" ", ""))}')
print(f'Total de letras do primeiro nome: {len(nomecompleto.split()[0])}')
#print(f'Total de letras sem espaços: ', len(nomecompleto) - nomecompleto.count(' '))
#print(f'Total de letras do primeiro nome: ', nomecompleto.find(' '))





