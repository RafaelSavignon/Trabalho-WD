# exercicio_2_4.py

# Pedindo ao usuário para digitar um ano
ano = int(input("Digite um ano: "))

# Verificando se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, "não é um ano bissexto.")
