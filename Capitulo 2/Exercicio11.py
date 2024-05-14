# exercicio_2_11.py

# Pedindo ao usuário para digitar a idade e a nacionalidade
idade = int(input("Digite sua idade: "))
nacionalidade = input("Digite sua nacionalidade: ")

# Verificando se a pessoa pode votar
if idade >= 16 and nacionalidade.lower() == 'brasileiro':
    print("Você pode votar.")
else:
    print("Você não pode votar.")
