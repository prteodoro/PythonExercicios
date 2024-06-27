from datetime import date

exercicio = ' Exercício 054 '
enunciado = """Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas 
pessoas ainda não atingiram a maioridade e quantas já são maiores."""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

menoresdeidade = 0
maioresdeidade = 0
for c in range(0, 7):
    anonascimento = int(input(f'Em que ano a {c + 1}ª pessoa nasceu? '))
    if anonascimento > date.today().year - 21:
        menoresdeidade += 1
    else:
        maioresdeidade += 1
print(f'Ao todo tivemos {maioresdeidade} pessoas maiores de idade')
print(f'E também tivemos {menoresdeidade} pessoas menores de idade')
