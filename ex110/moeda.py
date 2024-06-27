def aumentar(preco=0, taxa=0, form=False):
    res = preco + (preco * taxa/100)
    return res if form is False else moeda(res)


def diminuir(preco=0, taxa=0, form=False):
    res = preco - (preco * taxa/100)
    return res if not form else moeda(res)


def dobro(preco=0, form=False):
    res = preco * 2
    if form:
        return moeda(res)
    else:
        return res


def metade(preco=0, form=False):
    res = preco / 2
    if form:
        return moeda(res)
    else:
        return res


def moeda(preco=0, moeda='R$'):
    res = f'{moeda}{preco:>5.2f}'.replace('.', ',')
    return res

def resumo(preco=0, aumento=0, reducao=0):
    print('-'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-'*40)
    print(f'{"Preço analisado:":<25}{moeda(preco):>15}')
    print(f'{"Dobro do preço:":<25}{dobro(preco, True):>15}')
    print(f'{"Metade do preço:":<25}{metade(preco, True):>15}')
    print(f'{aumento:<2}{"% de aumento:":<23}{aumentar(preco, aumento, True):>15}')
    print(f'{reducao:<2}{"% de redução:":<23}{diminuir(preco, reducao, True):>15}')
    print('-'*40)
