import random


def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    while True:
        try:
            palpite = int(input("Digite um número entre 1 e 10: "))
            if palpite < 1 or palpite > 10:
                raise ValueError("Número fora do intervalo permitido.")
            break
        except ValueError as e:
            print(f"Erro: {e}")
    if palpite == numero_secreto:
        print("Parabéns, você acertou!")
    else:
        print(f"Que pena, o número secreto era {numero_secreto}.")


jogo_adivinhacao()
