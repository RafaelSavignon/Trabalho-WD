# Exercício 5.5: Variável definida dentro de uma função
def minha_funcao():
    x = 10
    print("O valor de x dentro da função é:", x)


# Chamada da função
minha_funcao()

# Tentativa de acessar a variável x fora da função
print("O valor de x fora da função é:", x)
