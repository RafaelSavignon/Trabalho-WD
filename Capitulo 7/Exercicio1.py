# Exercício 7.1: Solicitar ao usuário um nome de arquivo e exibir seu conteúdo na tela
nome_arquivo = input("Digite o nome do arquivo: ")
try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
