# exercicio_4_10.py
import re

# Pedindo ao usuário para digitar uma frase
frase = input("Digite uma frase: ")

# Usando expressão regular para extrair todos os artigos da frase
artigos = re.findall(r'\b(a|o|as|os)\b', frase, flags=re.IGNORECASE)

# Removendo os artigos da frase
frase_sem_artigos = re.sub(r'\b(a|o|as|os)\b', '', frase, flags=re.IGNORECASE)

# Mostrando os artigos encontrados e a frase sem os artigos
print("Artigos encontrados:", artigos)
print("Frase sem os artigos:", frase_sem_artigos)
