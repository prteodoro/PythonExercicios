import urllib.request

exercicio = ' Exercício 114 '
enunciado = """Crie um código em Python que teste se o site Pudim está acessível pelo computador usado."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

try:
    url = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.request.URLError:
    print(f'\033[31mO site pudim não está acessível no momento.\033[m')
else:
    print(f'\033[32mO site pudim está acessível.\033[m')
    print(url.read())
