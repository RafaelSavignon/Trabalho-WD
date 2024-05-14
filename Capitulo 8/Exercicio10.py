class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")


class Cliente(Pessoa):
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade)
        self.endereco = endereco

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Endereço: {self.endereco}")


# Criando uma instância da classe Cliente
cliente = Cliente("Maria", 30, "Rua A, 123")

# Chamando o método mostrar_dados da classe Cliente
cliente.mostrar_dados()
