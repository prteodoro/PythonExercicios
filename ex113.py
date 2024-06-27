exercicio = ' Exercício 113 '
enunciado = """Reescreva a função leiaInt() que fizemos no desafio 104, incluindo 
agora a possibilidade da digitação de um número de tipo inválido. Aproveite e 
crie também uma função leiaFloat() com a mesma funcionalidade."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            numreal = float(input(msg))
        except KeyboardInterrupt:
            print(f'\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print(f'\033[31mERRO! por favor, digite um número real válido.\033[m')
            continue
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')
        else:
            return numreal


nint = leiaInt('Digite um Inteiro: ')
nfloat = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {nint} e o real foi {nfloat}.')
