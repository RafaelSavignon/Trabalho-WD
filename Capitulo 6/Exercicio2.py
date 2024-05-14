# Exercício 6.2: List Comprehension para criar uma lista com as palavras que contêm a letra "a" em uma frase digitada pelo usuário, substituindo a letra por "o"
frase = input("Digite uma frase: ")
palavras_com_a = [palavra.replace('a', 'o')
                  for palavra in frase.split() if 'a' in palavra]
print("Palavras com 'a' substituído por 'o':", palavras_com_a)
