# Exercício 7.4: Renomear um arquivo adicionando a palavra "renomeado" ao nome existente, mantendo a extensão
import os

nome_arquivo = input("Digite o nome do arquivo a ser renomeado: ")

if os.path.exists(nome_arquivo):
    nome_arquivo_renomeado = nome_arquivo.split(
        '.')[0] + "_renomeado." + nome_arquivo.split('.')[1]
    os.rename(nome_arquivo, nome_arquivo_renomeado)
    print(f"Arquivo renomeado para '{nome_arquivo_renomeado}'.")
else:
    print("Arquivo não encontrado.")
