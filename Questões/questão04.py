# Questão 4

# Escreva um programa Python que leia o nome e a cidade do usuário e exiba uma mensagem de boas-vindas usando f-string.

# Exemplo de entrada:

# Ana
# Natal

# Exemplo de saída:
# Bem-vinda(o) a avaliação de ILP, Ana! Você é de Natal.

Nome = input('Insira seu nome: ')
Cidade = input('Insira sua cidade: ')

print(f'\nBem-vindo(a) a avaliação de ILP, {Nome}! Você é de {Cidade}.')