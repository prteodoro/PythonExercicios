exercicio = ' Exercício 067 '
enunciado = """Faça um programa que mostre a tabuada de vários números, um de cada vez, para 
cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado 
for negativo."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    print('-'*50)
    contador = 1
    while contador < 11:
        print(f'{valor} x {contador} = {valor * contador}')
        contador += 1
    print('-' * 50)
print('-' * 50)
print(f'PROGRAMA TABUADA ENCERRADO. Volte sempre!')
