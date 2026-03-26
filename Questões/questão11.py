# Questão 11 — Desafio 🏆
# Escreva um programa Python que leia para 15 alunos uma série de 4 números inteiros e o nome do aluno representando as notas em 4 bimestres de um aluno. O programa deve:

# Calcular a média das notas.
# Usar if else para determinar a situação: Aprovado (média ≥ 6), Recuperação (4 ≤ média < 6) ou Reprovado (média < 4).
# Usar um laço while ou for para percorrer os dados dos alunos e imprimir cada uma no formato de linha CSV (separadas por ; e com end=';'), exibindo ao final a média e a situação também separadas por ;.
Exemplo de entrada:

7 5 8 6 Fulano
7.1 5.2 8.3 6.4 Cicrano
7 5 8 6 FulanoCicrano
7.1 5.2 8.3 6.4 CicranoFulano
1 2 3 4 CFulano
4 3 2 1 FCicrano
4 4 4 4 CF
5.9 5.9 5.9 5.9 FC
...
Exemplo de saída:

7;5;8;6;6.5;Aprovado;Fulano
7.1;5.2;8.3;6.4;6,75;Aprovado;Cicrano
7;5;8;6;6.5;Aprovado;FulanoCicrano
7.1;5.2;8.3;6.4;6.75;Aprovado;CicranoFulano
1;2;3;4;2.5;Reprovado;CFulano
4;3;2;1;2.5;Reprovado;FCicrano
4;4;4;4;4.0;Recuperação;CF
5.9;5.9;5.9;5.9;5.9;Recuperação;FC
...
;Dica: se preferir no lugar de fazer print(valor, end=';') use f-string para imprimir sem quebra de linha e separando os valores com ;.