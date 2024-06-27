exercício = ' Exercício 031 '
enunciado = """Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da 
passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas."""
fim = '='*30
print(f'{exercício:=^30} \n{enunciado} \n{fim}')

distancia = float(input('Qual é a distância da sua viagem? '))

print(f'Você está prestes a começar uma viagem de {distancia:.0f}Km')
if distancia > 200:
    valorpassagem = distancia * 0.45
else:
    valorpassagem = distancia * 0.50
print(f'E o preço da sua passagem será de R${valorpassagem:.2f}')

#Solução simplificada
print(f'\nSOLUÇÃO SIMPLIFICADA')
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preço da sua passagem será de R${preco:.2f}')

