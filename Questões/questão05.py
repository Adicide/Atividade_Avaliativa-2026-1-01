# Questão 5

# Escreva um programa Python que leia o nome e o curso do usuário e exiba uma mensagem de apresentação usando f-string.

# Exemplo de entrada:
# Carlos
# Infoweb

# Exemplo de saída: 
# Olá! Meu nome é Carlos e estou matriculado no curso Infoweb.

Nome = input('Qual o seu nome?\n')
Curso = input('\nExcelente. E o qual o seu curso?\n')

print(f'\nOlá! Meu nome é {Nome} e estou matriculado no curso {Curso}.')