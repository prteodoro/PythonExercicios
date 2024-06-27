exercicio = ' Exercício 079 '
enunciado = """Crie um programa onde o usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

valores = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor in valores:
        print(f'Valor duplicado! Não vou adicionar...')
    else:
        valores.append(valor)
        print(f'Valor adicionado com sucesso...')
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-='*25)
valores.sort()
print(f'Você digitou os valores {valores}')
