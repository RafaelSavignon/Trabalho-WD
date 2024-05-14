# exercicio_4_7.py
import re

# Pedindo ao usuário para digitar um nome de usuário e uma senha
usuario = input("Digite um nome de usuário: ")
senha = input("Digite uma senha (contendo apenas caracteres alfanuméricos): ")

# Aplicando expressões regulares para limpar os valores digitados
usuario_limpo = re.sub(r'\W+', '', usuario)
senha_limpa = re.sub(r'\W+', '', senha)

# Mostrando os valores processados
print("Nome de usuário processado:", usuario_limpo)
print("Senha processada:", senha_limpa)
