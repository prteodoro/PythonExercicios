def leiaDinheiro(msg):
    res = str(input('Digite o valor: ')).strip().replace(',', '.')
    while not res.replace('.', '').isdigit():
        print(f'\033[31mERRO: "{res}" é um preço inválido!\033[m')
        res = str(input('Digite o valor: ')).strip().replace(',', '.')
    res = float(res)
    return res

