exercicio = ' Exercício 102 '
enunciado = """Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o 
primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico 
(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print('-'*30)
print(fatorial(6, True))
help(fatorial)