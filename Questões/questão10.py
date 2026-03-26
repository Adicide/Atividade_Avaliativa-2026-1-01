# Questão 10

# Escreva um programa Python que leia 4 números inteiros e use o if else para verificar se a média deles é maior ou igual a 6. Exiba dois prints usando f-string: um com o valor da média e outro indicando se o aluno foi aprovado (média ≥ 6) ou reprovado (média < 6).

# Exemplo de entrada:
# 8
# 5
# 7
# 6

# Exemplo de saída (quando aprovado):
# A média é: 6.5
# Situação: Aprovado(a)!

num1=int(input('Insira o 1° número: '))
num2=int(input('Insira o 2° número: '))
num3=int(input('Insira o 3° número: '))
num4=int(input('Insira o 4° número: '))

média = (num1+num2+num3+num4)/4
print(f'\nSua média é: {média}')

if média >= 6:
    print('Situação: Aprovado!')
else:
    print('Situação: Reprovado!')