# Exercício 6.8: Mapeamento para retornar uma nova lista com os quadrados de cada número
def calcular_quadrado(numero):
    return numero ** 2


# Pedindo ao usuário para digitar uma lista de números
numeros = input("Digite uma lista de números separados por espaço: ").split()

# Convertendo os números para inteiros e calculando os quadrados usando mapeamento
quadrados = list(map(lambda x: calcular_quadrado(int(x)), numeros))

# Mostrando a lista com os quadrados dos números
print("Quadrados dos números:", quadrados)
