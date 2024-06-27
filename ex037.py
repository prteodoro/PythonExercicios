exercício = ' Exercício 037 '
enunciado = """Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual 
será a base de conversão:
	- 1 para binário
	- 2 para octal
	- 3 para hexadecimal"""
fim = '=' * 30
print(f'{exercício:=^30} \n{enunciado} \n{fim}')

num = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
opcaoescolhida = int(input(f'Sua opção: '))
if opcaoescolhida == 1:
    print(f'{num} convertido para BINÁRIO é igual a {num:b}')
elif opcaoescolhida == 2:
    print(f'{num} convertido para OCTAL é igual a {num:o}')
elif opcaoescolhida == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {num:x}')
else:
    print(f'Opção inválida. Tente novamente.')
