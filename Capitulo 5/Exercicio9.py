# Exercício 5.9: Filtrando vinhos por preço usando uma função lambda
# Criando uma lista de vinhos com seus preços
vinhos = [
    {"nome": "Vinho Tinto", "preco": 60},
    {"nome": "Vinho Branco", "preco": 45},
    {"nome": "Espumante", "preco": 80},
    {"nome": "Rosé", "preco": 35},
    {"nome": "Vinho do Porto", "preco": 100}
]

# Usando uma função lambda para filtrar os vinhos com preço maior que 50
vinhos_caros = list(filter(lambda vinho: vinho["preco"] > 50, vinhos))

# Imprimindo a lista de vinhos caros
print("Vinhos caros:")
for vinho in vinhos_caros:
    print(vinho["nome"], "-", "R$ {:.2f}".format(vinho["preco"]))
