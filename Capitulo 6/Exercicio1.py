# Exercício 6.1: List Comprehension para criar uma lista com as raízes quadradas dos números pares de 0 a 20
raizes_quadradas = [round((x ** 0.5), 2) for x in range(0, 21) if x % 2 == 0]
print("Raízes quadradas dos números pares de 0 a 20:", raizes_quadradas)
