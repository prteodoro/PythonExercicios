exercicio = ' Exercício 025 '
enunciado = 'Crie um programa que leia o nome de uma pessoa e diga se ela tem (SILVA) no nome.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

nome = str(input("Digite um nome completo: ")).strip().title().split()
print(f'Esse nome tem (Silva): ', 'Silva' in nome)
