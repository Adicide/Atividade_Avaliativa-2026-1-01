# Questão 11 — Desafio 🏆
# Escreva um programa Python que leia para 15 alunos uma série de 4 números inteiros e o nome do aluno representando as notas em 4 bimestres de um aluno. O programa deve:

# Calcular a média das notas.
# Usar if else para determinar a situação: Aprovado (média ≥ 6), Recuperação (4 ≤ média < 6) ou Reprovado (média < 4).
# Usar um laço while ou for para percorrer os dados dos alunos e imprimir cada uma no formato de linha CSV (separadas por ; e com end=';'), exibindo ao final a média e a situação também separadas por ;.
# Exemplo de entrada:

# 7 5 8 6 Fulano
# 7.1 5.2 8.3 6.4 Cicrano
# 7 5 8 6 FulanoCicrano
# 7.1 5.2 8.3 6.4 CicranoFulano
# 1 2 3 4 CFulano
# 4 3 2 1 FCicrano
# 4 4 4 4 CF
# 5.9 5.9 5.9 5.9 FC
# ...

# Exemplo de saída:
# 7;5;8;6;6.5;Aprovado;Fulano
# 7.1;5.2;8.3;6.4;6,75;Aprovado;Cicrano
# 7;5;8;6;6.5;Aprovado;FulanoCicrano
# 7.1;5.2;8.3;6.4;6.75;Aprovado;CicranoFulano
# 1;2;3;4;2.5;Reprovado;CFulano
# 4;3;2;1;2.5;Reprovado;FCicrano
# 4;4;4;4;4.0;Recuperação;CF
# 5.9;5.9;5.9;5.9;5.9;Recuperação;FC
# ...

# ;Dica: se preferir no lugar de fazer print(valor, end=';') use f-string para imprimir sem quebra de linha e separando os valores com ;.

Aluno1= 'Ana'
Aluno2= 'João'
Aluno3= 'Roberto'
Aluno4= 'Samuel'
Aluno5= 'Lucas'
Aluno6= 'Thiago'
Aluno7= 'Matheus'
Aluno8= 'Luna'
Aluno9= 'Sara'
Aluno10= 'Maria'
Aluno11= 'Humberto'
Aluno12= 'José'
Aluno13= 'Helena'
Aluno14= 'Marcos'
Aluno15= 'Júlia'

NotasAluno1=Nota1Aluno1, Nota2Aluno1, Nota3Aluno1, Nota4Aluno1
NotasAluno2=Nota1Aluno2, Nota2Aluno2, Nota3Aluno2, Nota4Aluno2
NotasAluno3=Nota1Aluno3, Nota2Aluno3, Nota3Aluno3, Nota4Aluno3
NotasAluno4=Nota1Aluno4, Nota2Aluno4, Nota3Aluno4, Nota4Aluno4
NotasAluno5=Nota1Aluno5, Nota2Aluno5, Nota3Aluno5, Nota4Aluno5
NotasAluno6=Nota1Aluno6, Nota2Aluno6, Nota3Aluno6, Nota4Aluno6
NotasAluno7=Nota1Aluno7, Nota2Aluno7, Nota3Aluno7, Nota4Aluno7
NotasAluno8=Nota1Aluno8, Nota2Aluno8, Nota3Aluno8, Nota4Aluno8
NotasAluno9=Nota1Aluno9, Nota2Aluno9, Nota3Aluno9, Nota4Aluno9
NotasAluno10=Nota1Aluno10, Nota2Aluno10, Nota3Aluno10, Nota4Aluno10
NotasAluno11=Nota1Aluno11, Nota2Aluno11, Nota3Aluno11, Nota4Aluno11
NotasAluno12=Nota1Aluno12, Nota2Aluno12, Nota3Aluno12, Nota4Aluno12
NotasAluno13=Nota1Aluno13, Nota2Aluno13, Nota3Aluno13, Nota4Aluno13
NotasAluno14=Nota1Aluno14, Nota2Aluno14, Nota3Aluno14, Nota4Aluno14
NotasAluno15=Nota1Aluno15, Nota2Aluno15, Nota3Aluno15, Nota4Aluno15

Nota1Aluno1, Nota2Aluno1, Nota3Aluno1, Nota4Aluno1= map(int(input('Notas do 1° aluno: ')).split())
Nota1Aluno2, Nota2Aluno2, Nota3Aluno2, Nota4Aluno2= map(int(input('Notas do 2° aluno: ')).split())
Nota1Aluno3, Nota2Aluno3, Nota3Aluno3, Nota4Aluno3= map(int(input('Notas do 3° aluno: ')).split())
Nota1Aluno4, Nota2Aluno4, Nota3Aluno4, Nota4Aluno4= map(int(input('Notas do 4° aluno: ')).split())
Nota1Aluno5, Nota2Aluno5, Nota3Aluno5, Nota4Aluno5= map(int(input('Notas do 5° aluno: ')).split())
Nota1Aluno6, Nota2Aluno6, Nota3Aluno6, Nota4Aluno6= map(int(input('Notas do 6° aluno: ')).split())
Nota1Aluno7, Nota2Aluno7, Nota3Aluno7, Nota4Aluno7= map(int(input('Notas do 7° aluno: ')).split())
Nota1Aluno8, Nota2Aluno8, Nota3Aluno8, Nota4Aluno8= map(int(input('Notas do 8° aluno: ')).split())
Nota1Aluno9, Nota2Aluno9, Nota3Aluno9, Nota4Aluno9= map(int(input('Notas do 9° aluno: ')).split())
Nota1Aluno10, Nota2Aluno10, Nota3Aluno10, Nota4Aluno10= map(int(input('Notas do 10° aluno: ')).split())
Nota1Aluno11, Nota2Aluno11, Nota3Aluno11, Nota4Aluno11= map(int(input('Notas do 11° aluno: ')).split())
Nota1Aluno12, Nota2Aluno12, Nota3Aluno12, Nota4Aluno12= map(int(input('Notas do 12° aluno: ')).split())
Nota1Aluno13, Nota2Aluno13, Nota3Aluno13, Nota4Aluno13= map(int(input('Notas do 13° aluno: ')).split())
Nota1Aluno14, Nota2Aluno14, Nota3Aluno14, Nota4Aluno14= map(int(input('Notas do 14° aluno: ')).split())
Nota1Aluno15, Nota2Aluno15, Nota3Aluno15, Nota4Aluno15= map(int(input('Notas do 15° aluno: ')).split())

if NotasAluno1 >= 6:
    print('Aprovado')
else:
    print('Reprovado')
