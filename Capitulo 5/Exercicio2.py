# Exercício 5.2: Função para verificar se um número é par ou ímpar
def eh_par(numero):
    return numero % 2 == 0


# Chamada da função com argumento
numero = int(input("Digite um número para verificar se é par ou ímpar: "))
if eh_par(numero):
    print(numero, "é par.")
else:
    print(numero, "é ímpar.")
