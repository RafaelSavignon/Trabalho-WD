def jogo_adivinhacao_palavra():
    palavra_secreta = "python"
    while True:
        try:
            palpite = input("Digite uma letra: ").lower()
            if not palpite.isalpha() or len(palpite) != 1:
                raise ValueError("Digite apenas uma letra do alfabeto.")
            break
        except ValueError as e:
            print(f"Erro: {e}")
    if palpite == palavra_secreta:
        print("Parabéns, você acertou a palavra secreta!")
    else:
        print(f"Que pena, a palavra secreta era {palavra_secreta}.")


jogo_adivinhacao_palavra()
