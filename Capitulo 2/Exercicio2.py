# exercicio_2_2.py

# Pedindo ao usuário para digitar um número
numero = float(input("Digite um número: "))

# Verificando se o número é positivo, negativo ou zero
if numero > 0:
    print(numero, "é um número positivo.")
elif numero < 0:
    print(numero, "é um número negativo.")
else:
    print("O número digitado é zero.")
