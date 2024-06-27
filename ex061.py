exercicio = ' Exercício 061 '
enunciado = """Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 
primeiros termos da progressão usando a estrutura while."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

print(f'Gerador de PA')
print('-='*10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 0
while contador <= 10:
    print(termo, '→ ', end='')
    termo += razao
    contador += 1
print('FIM')
