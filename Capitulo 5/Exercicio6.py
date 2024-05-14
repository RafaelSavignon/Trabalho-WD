# Exercício 5.6: Programa para adicionar um elemento a uma lista
def adicionar(lista):
    novo_elemento = input("Digite um novo elemento para adicionar à lista: ")
    lista.append(novo_elemento)


# Declarando uma lista inicial com 5 números inteiros
idades = [18, 25, 30, 40, 50]

# Chamando a função adicionar e passando a lista idades como argumento
adicionar(idades)

# Mostrando a lista para verificar se o elemento foi adicionado corretamente
print("Lista de idades após adicionar um novo elemento:", idades)
