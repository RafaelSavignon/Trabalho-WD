# Exercício 7.8: Excluir o diretório criado no exercício anterior com todo o seu conteúdo
import os
import shutil

nome_diretorio = "temp"

if os.path.exists(nome_diretorio):
    shutil.rmtree(nome_diretorio)
    print(
        f"Diretório '{nome_diretorio}' e todo o seu conteúdo foram excluídos com sucesso.")
else:
    print(f"Diretório '{nome_diretorio}' não encontrado.")
