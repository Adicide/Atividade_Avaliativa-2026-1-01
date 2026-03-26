# Questão 9

# Escreva um programa Python que leia 4 números reais e use o if para verificar se o produto deles é positivo. Exiba dois prints usando f-string: um com o valor do produto e outro indicando se ele é positivo ou não.

# Exemplo de entrada:
# 2.0
# 3.0
# -1.0
# 4.0

# Exemplo de saída (quando o produto não for positivo):
# O produto dos 4 números é: -24.0
# O produto não é positivo.

num1=float(input('Insira o 1° número: '))
num2=float(input('Insira o 2° número: '))
num3=float(input('Insira o 3° número: '))
num4=float(input('Insira o 4° número: '))
prodnums=num1*num2*num3*num4

print(f'\nO produto dos 4 números é: {prodnums}')
if prodnums >= 0:
    print(f'O produto é positivo.')
else:
    print('O produto não é positivo.')