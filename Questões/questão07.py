# Questão 7

# Escreva um programa Python que leia 4 números reais e exiba a média aritmética e a diferença entre o maior e o menor valor usando f-string.

# Exemplo de entrada:
# 10.0
# 6.0
# 8.0
# 4.0

# Exemplo de saída:
# A média aritmética é: 7.0
# A diferença entre o maior e o menor valor é: 6.0

num1= float(input('Insira o 1° número: '))
num2= float(input('Insira o 2° número: '))
num3= float(input('Insira o 3° número: '))
num4= float(input('Insira o 4° número: '))

nums = [num1, num2, num3, num4]
maiornum = max(nums)
menornum = min(nums)

média_aritmética= (num1+num2+num3+num4)/4
diferença = maiornum - menornum

print(f'\nA média aritmética é: {média_aritmética}')
print(f'A diferença entre o maior e o menor valor é: {diferença}') 