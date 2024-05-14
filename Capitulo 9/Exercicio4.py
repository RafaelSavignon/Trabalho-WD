class SaldoInsuficienteError(Exception):
    pass


class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(
                "Saldo insuficiente para realizar o saque.")
        self.saldo -= valor


# Testando a classe ContaBancaria
conta = ContaBancaria(1000)
try:
    conta.sacar(1500)
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")
else:
    print("Saque realizado com sucesso.")
