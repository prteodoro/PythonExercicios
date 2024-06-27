exercicio = ' Exercício 024 '
enunciado = 'Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome (SANTO).'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

cidade = str(input(f'Digite o nome da cidade: ')).lstrip()
print(f'O nome da cidade começa com (Santo):', 'Santo' in cidade.capitalize().split()[0])

#Outra solução
#print(cidade[:5].capitalize() == 'Santo')
