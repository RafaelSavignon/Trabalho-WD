# exercicio_4_6.py

# Pedindo ao usuário para inserir dois números complexos
numero_complexo1 = complex(
    input("Digite o primeiro número complexo (no formato a+bj): "))
numero_complexo2 = complex(
    input("Digite o segundo número complexo (no formato a+bj): "))

# Calculando a soma e o produto dos números complexos
soma = numero_complexo1 + numero_complexo2
produto = numero_complexo1 * numero_complexo2

# Mostrando a soma e o produto dos números complexos
print("A soma dos números complexos é:", soma)
print("O produto dos números complexos é:", produto)
