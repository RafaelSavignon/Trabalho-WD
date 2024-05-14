# Exercício 7.3: Ler um arquivo texto, inverter o conteúdo de cada linha e salvar em um novo arquivo
nome_arquivo_origem = input("Digite o nome do arquivo de origem: ")
nome_arquivo_destino = input("Digite o nome do arquivo de destino: ")

try:
    with open(nome_arquivo_origem, 'r') as arquivo_origem:
        linhas_invertidas = [linha[::-1] for linha in arquivo_origem]

    with open(nome_arquivo_destino, 'w') as arquivo_destino:
        arquivo_destino.writelines(linhas_invertidas)

    print("Conteúdo invertido salvo com sucesso.")
except FileNotFoundError:
    print("Arquivo de origem não encontrado.")
