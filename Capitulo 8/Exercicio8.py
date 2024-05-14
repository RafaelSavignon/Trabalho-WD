class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Matrícula: {self.matricula}")


# Criando uma instância da classe Aluno
aluno = Aluno("João", 20, "2021001")

# Chamando o método mostrar_dados da classe Aluno
aluno.mostrar_dados()
