# exercicio_3_7.py

# Inicializando as variáveis para armazenar a soma e a contagem dos números positivos
soma = 0
contador = 0

# Pedindo ao usuário para digitar os números
print("Digite números positivos. Digite um número negativo para parar.")

while True:
    numero = float(input("Digite um número: "))

    # Verificando se o número é positivo
    if numero >= 0:
        soma += numero
        contador += 1
    else:
        break

# Calculando a média dos números positivos
if contador > 0:
    media = soma / contador
    print("A média dos números positivos digitados é:", media)
else:
    print("Nenhum número positivo foi digitado.")
