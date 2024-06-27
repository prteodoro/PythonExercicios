exercicio = ' Exercício 057 '
enunciado = """Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F': #while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
