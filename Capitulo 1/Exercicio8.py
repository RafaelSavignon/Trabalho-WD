# exercicio_1_8.py
import math

# Pedindo ao usuário para digitar um ângulo entre 0 e 360 graus
angulo = float(input("Digite um ângulo entre 0 e 360 graus: "))

# Convertendo o ângulo para radianos
angulo_radianos = math.radians(angulo)

# Calculando o seno, cosseno e tangente do ângulo
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Imprimindo o resultado
print("O seno de", angulo, "graus é:", seno)
print("O cosseno de", angulo, "graus é:", cosseno)
print("A tangente de", angulo, "graus é:", tangente)
