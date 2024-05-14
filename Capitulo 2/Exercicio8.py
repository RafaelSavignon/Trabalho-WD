# exercicio_2_8.py

# Pedindo ao usuário para digitar uma data no formato "dd/mm/aaaa"
data = input("Digite uma data no formato 'dd/mm/aaaa': ")

# Verificando se a data possui o formato correto
if len(data) == 10 and data[2] == '/' and data[5] == '/':
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:])

    # Verificando se os valores de dia, mês e ano estão dentro do intervalo correto
    if (1 <= dia <= 31) and (1 <= mes <= 12) and (1 <= ano <= 9999):
        print("A data digitada é válida.")
    else:
        print("A data digitada não é válida.")
else:
    print("A data digitada não possui o formato correto.")
