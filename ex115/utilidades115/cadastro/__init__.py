from time import sleep

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
                print(f'Opção 01')
                return listar()
            elif opcao == 2:
                print(f'Opção 02')
                return cadastar()
            elif opcao == 3:
                print(f'Opção 03')
                return sair(opcao)
            else:
                print(f'\033[31mERRO: Digite uma opção válida entre 1 e 3.\033[m')


def listar():
    print('-'*40)
    print(f'{"PESSOAS CADASTRADAS":^40}')
    print('-'*40)
    sleep(1)
    try:
        with open('Clients02.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<30} {dado[1]:>3} anos')
                sleep(0.1)
    except FileNotFoundError:
        print(f'\033[31mAinda não tem nenhuma pessoa cadastrada.\033[m')
    menuprincipal()
    return leiaopcao('\033[33mSua Opção:\033[m ')


def cadastar():
    print('-'*40)
    print(f'{"NOVO CADASTRO":^40}')
    print('-'*40)
    with open('Clients02.txt', 'a', encoding='utf-8') as arquivo:
        pessoa = []
        try:
            nome = str(input('Nome: ').strip().title())[0:30]
            while True:
                try:
                    idade = int(input('Idade: '))
                except (ValueError, TypeError):
                    print(f'\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
                except Exception as erro:
                    print(f'O erro encontrado foi {erro}')
                except KeyboardInterrupt:
                    print(f'\033[31mO usuário desisitiu de completar o cadastro.\033[m')
                    break
                else:
                    pessoa.append(nome)
                    pessoa.append(idade)
                    arquivo.writelines(f'{pessoa[0]};{pessoa[1]}\n')
                    print(f'Novo registro de {pessoa[0]} adicionado.')
                    break
        except KeyboardInterrupt:
            print(f'\033[31mO usuário desisitiu de completar o cadastro.\033[m')
    menuprincipal()
    leiaopcao('\033[33mSua Opção:\033[m ')


def sair(msg):
    print('-'*40)
    print(f'{"Saindo do sistema... Até logo!":^40}')
    print('-'*40)
