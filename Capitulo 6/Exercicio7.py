# Exercício 6.7: Dict Comprehension para arredondar as notas dos alunos para o número inteiro mais próximo
num_alunos = int(input("Digite o número de alunos: "))

# Criando o dicionário com nomes e notas dos alunos
alunos_notas = {input("Digite o nome do aluno: "): float(
    input("Digite a nota do aluno: ")) for _ in range(num_alunos)}

# Criando um novo dicionário com as notas arredondadas dos alunos
alunos_notas_arredondadas = {aluno: round(
    nota) for aluno, nota in alunos_notas.items()}

# Mostrando o dicionário com as notas arredondadas
print("Notas arredondadas dos alunos:", alunos_notas_arredondadas)
