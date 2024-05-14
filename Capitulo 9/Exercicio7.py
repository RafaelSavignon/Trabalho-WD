class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            raise ValueError("Os lados do triângulo devem ser positivos.")
        if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
            raise ValueError(
                "Os lados fornecidos não formam um triângulo válido.")
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"


try:
    triangulo = Triangulo(3, 4, 5)
    print("Tipo do triângulo:", triangulo.tipo_triangulo())
except ValueError as e:
    print(f"Erro: {e}")
