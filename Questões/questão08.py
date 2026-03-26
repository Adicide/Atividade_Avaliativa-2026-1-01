# Questão 8

# Escreva um programa Python que leia 4 números inteiros e use o if para verificar se a soma deles é maior que 100. Exiba dois prints usando f-string: um com o valor da soma e outro informando se ela é maior que 100 ou não.

# Exemplo de entrada:
# 30
# 40
# 20
# 15

# Exemplo de saída (quando a soma for maior que 100):
# A soma dos 4 números é: 105
# A soma é maior que 100.


num1=int(input('Digite o 1° número: '))
num2=int(input('Digite o 2° número: '))
num3=int(input('Digite o 3° número: '))
num4=int(input('Digite o 4° número: '))

somanums=num1+num2+num3+num4

print(f'\nA soma dos 4 números é: {somanums}')

if somanums > 100:
    print('A soma é maior que 100.')
elif somanums == 100:
    print('A soma é igual a 100.')
else:
    print('A soma é menor que 100.')