class Carro:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self, segundos):
        aceleracao = 10
        self.velocidade += aceleracao * segundos

    def frear(self, segundos):
        desaceleracao = 5
        velocidade_reduzida = desaceleracao * segundos
        self.velocidade = max(0, self.velocidade - velocidade_reduzida)

    def mostrar_velocidade(self):
        print("Velocidade atual:", self.velocidade)


# Criando uma instância da classe Carro
carro = Carro()

# Testando os métodos criados
carro.acelerar(5)
carro.mostrar_velocidade()
carro.frear(3)
carro.mostrar_velocidade()
