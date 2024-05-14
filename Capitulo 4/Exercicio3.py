# exercicio_4_3.py
import math

# Pedindo ao usuário para inserir um ângulo em graus
angulo_graus = float(input("Digite um ângulo em graus: "))

# Convertendo o ângulo para radianos
angulo_radianos = math.radians(angulo_graus)

# Calculando o seno, cosseno e tangente do ângulo
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Mostrando os resultados
print("O seno do ângulo é:", seno)
print("O cosseno do ângulo é:", cosseno)
print("A tangente do ângulo é:", tangente)
