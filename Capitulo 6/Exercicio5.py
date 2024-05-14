# Exercício 6.5: Dicionário com notas de alunos e Dict Comprehension para criar um dicionário com os alunos com nota igual ou superior a 7
num_alunos = int(input("Digite o número de alunos: "))

# Criando o dicionário com nomes e notas dos alunos
alunos_notas = {input("Digite o nome do aluno: "): float(
    input("Digite a nota do aluno: ")) for _ in range(num_alunos)}

# Criando um novo dicionário com alunos com nota igual ou superior a 7
alunos_aprovados = {aluno: nota for aluno,
                    nota in alunos_notas.items() if nota >= 7}

# Mostrando o dicionário com os alunos aprovados
print("Alunos aprovados:", alunos_aprovados)
