exercicio = ' Exercício 104 '
enunciado = """Crie um programa que tenha uma função leiaint(), que vai funcionar de forma semelhante 
à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex.: n = leiaint('Digite um n')"""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')


def leiaInt(msg):
    while True:
        num = str(input(msg)).strip()
        if num.isnumeric():
            break
        else:
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
    return num
print('-'*30)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
