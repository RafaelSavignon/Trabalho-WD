class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura


# Criando uma instância da classe Retangulo
retangulo = Retangulo(5, 3)

# Chamando o método area e exibindo a área do retângulo
print("Área do retângulo:", retangulo.area())
