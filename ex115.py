from time import sleep

exercicio = ' Exercício 115 '
enunciado = """Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome 
e idade em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')


"""lista = [{'Nome': 'Ana Paula', 'Idade': 32},
         {'Nome': 'Cláudio Mendonça', 'Idade': 32},
         {'Nome': 'Gustavo Guanabara', 'Idade': 41},
         {'Nome': 'Maria Clara Peixoto', 'Idade': 65},
         {'Nome': 'Maurício Souza', 'Idade': 19},
         {'Nome': 'Nilce Pedrosa', 'Idade': 43},
         {'Nome': 'Pedro Gonçalves', 'Idade': 18},
         {'Nome': 'Rafael Albuquerque', 'Idade': 38},
         {'Nome': 'Renata Soares', 'Idade': 13}]"""
pessoa = {}


def menuprincipal():
    print('-' * 40)
    print(f'{"MENU PRINCIPAL":^40}')
    print('-' * 40)
    sleep(0.3)
    print(f'\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print(f'\033[33m2\033[m - \033[34mCadastrar nova pessoa\033[m')
    print(f'\033[33m3\033[m - \033[34mSair do Sistema\033[m')
    print('-' * 40)
    sleep(0.3)
    return leiaopcao('\033[33mSua Opção:\033[m ')


def leiaopcao(msg):
    while True:
        try:
            opcao = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mO usuário não digitou nenhuma opção e saiu do sistema.\033[m')
        else:
            if opcao == 1:
                return listar()
            elif opcao == 2:
                return cadastar()
            elif opcao == 3:
                return sair(opcao)
            else:
                print(f'\033[31mERRO: Digite uma opção válida entre 1 e 3.\033[m')


def listar():
    print('-'*40)
    print(f'{"PESSOAS CADASTRADAS":^40}')
    print('-'*40)
    sleep(1)
    """for v in lista:
        for k, valor in v.items():
            if k == 'Nome':
                print(f'{valor:<25}', end='')
            elif k == 'Idade':
                print(f'{valor:>9} anos', end='')
        sleep(0.3)
        print()"""
    with open('Clients02.txt', 'r', encoding='utf-8') as arquivo:
        dados = arquivo.readlines()
    for v in dados:
        v = v.rstrip()
        if not v.isnumeric() :
            print(f'{v:<30}', end='')
        elif v.isnumeric():
            print(f'{v} anos')
        sleep(0.3)
    return menuprincipal()


def cadastar():
    print('-'*40)
    print(f'{"NOVO CADASTRO":^40}')
    print('-'*40)
    with open('Clients02.txt', 'a', encoding='utf-8') as arquivo:
        pessoa = []
        while True:
            try:
                nome = str(input('Nome: ').strip().title())
                idade = int(input('Idade: '))
            except (ValueError, TypeError):
                print(f'\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
            except Exception as erro:
                print(f'O erro encontrado foi {erro}')
            else:
                pessoa.append(nome)
                pessoa.append(idade)
                arquivo.writelines(f'\n{pessoa[0]} \n{pessoa[1]}')
                break
    print(f'Novo registro de {pessoa[0]} adicionado.')


    return menuprincipal()


def sair(msg):
    print('-'*40)
    print(f'{"Saindo do sistema... Até logo!":^40}')
    print('-'*40)


menuprincipal()
