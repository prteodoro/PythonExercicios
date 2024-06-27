exercicio = ' Exercício 101 '
enunciado = """Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('NÃO VOTA.')
    elif idade < 18 or idade > 65:
        print('VOTO OPCIONAL.')
    else:
        print('VOTO OBRIGATÓRIO.')


anonascimento = int(input('Em que ano você nasceu? '))
voto(anonascimento)
