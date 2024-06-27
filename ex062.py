exercicio = ' Exercício 062 '
enunciado = """Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais 
alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

print('Gerador de PA')
print('-='*20)
primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeirotermo
quantosmais = 10
total = 0
while quantosmais != 0:
    while total < quantosmais:
        print(termo, '→ ', end='')
        termo += razao
        total += 1
    print('PAUSA')
    quantosmais = int(input('Quantos termos você quer mostrar a mais? '))
    if quantosmais != 0:
        quantosmais += total
print(f'Progressão finalizada com {total} termos mostrados.')
