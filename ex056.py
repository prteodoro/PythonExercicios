exercicio = ' Exercício 056 '
enunciado = """Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa, mostre: 
	- A média de idade do grupo
	- Qual é o nome do homem mais velho
	- Quantas mulheres têm menos de 20 anos"""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

qtdmulheres20 = 0
idadehomemvelho = 0
nomehomemvelho = ''
totalpessoas = 0
somaidade = 0
mediaidade = 0
for c in range(1, 5):
    print(f'{"-" * 5} {c}ª PESSOA {"-"*5}')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    totalpessoas += 1
    somaidade += idade
    mediaidade = somaidade / totalpessoas
    if sexo == 'M' and idade > idadehomemvelho:
        nomehomemvelho = nome
        idadehomemvelho = idade
    elif sexo == 'F' and idade < 20:
        qtdmulheres20 += 1
print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {idadehomemvelho} anos e se chama {nomehomemvelho}.')
print(f'Ao todo são {qtdmulheres20} mulheres com menos de 20 anos.')





