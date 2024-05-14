def media_lista(lista):
    try:
        if not lista:
            raise ValueError("A lista está vazia.")
        numeros = [float(x) for x in lista]
        return sum(numeros) / len(numeros)
    except ValueError as e:
        print(f"Erro: {e}")
        return None


lista_numeros = input(
    "Digite uma lista de números separados por espaço: ").split()
print("Média:", media_lista(lista_numeros))
