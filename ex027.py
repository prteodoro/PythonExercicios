exercicio = ' Exercício 027 '
enunciado = """Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro 
e o último nome separadamente. Ex: Ana maria de Souza. primeiro: Ana último: Souza"""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

nomecompleto = str(input('Digite seu nome completo: ')).strip().upper().split()
print(f'Seu primeiro nome é {nomecompleto[0]}')
print(f'Seu último nome é {nomecompleto[len(nomecompleto) - 1]}')

#Outra solução para o último, -1 pega o último, -2 pega o antepenúltimo e assim vai
print('\nOutra solução para o último, -1 pega o último, -2 pega o antepenúltimo e assim vai')
print(f'Seu último nome é {nomecompleto[-1]}')


