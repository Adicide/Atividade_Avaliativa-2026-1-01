# Questão 6

# Escreva um programa Python que leia 4 números inteiros e exiba a soma e o produto deles usando f-string.

# Exemplo de entrada:
# 2
# 3
# 4
# 5

# Exemplo de saída:
# A soma dos números é: 14
# O produto dos números é: 120

num1= int(input('Insira o 1° número: '))
num2= int(input('Insira o 2° número: '))
num3= int(input('Insira o 3° número: '))
num4= int(input('Insira o 4° número: '))

somanums = num1+num2+num3+num4
prodnums = num1*num2*num3*num4

print(f'\nA soma dos números é: {somanums}')
print(f'O produto dos números é: {prodnums}')