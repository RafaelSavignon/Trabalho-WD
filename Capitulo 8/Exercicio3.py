class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print("Saldo atual:", self.saldo)


# Criando uma instância da classe ContaBancaria
conta = ContaBancaria()

# Testando os métodos criados
conta.depositar(100)
conta.exibir_saldo()
conta.sacar(50)
conta.exibir_saldo()
conta.sacar(100)
conta.exibir_saldo()
