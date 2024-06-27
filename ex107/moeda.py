def aumentar(preco, taxa=10):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco, taxa=5):
    res = preco - (preco * taxa/100)
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    return preco / 2
