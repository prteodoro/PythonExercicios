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

