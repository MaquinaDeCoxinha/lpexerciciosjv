class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir_ponto(self):
        print(f'Ponto(x={self.x}, y={self.y})')


class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)


def main():
    print("Programa de manipulação de retângulos")
    
    ponto_inicial = Ponto(0, 0)
    retangulo = Retangulo(ponto_inicial, 5, 3)

    while True:
        print("\nMenu:")
        print("1 - Alterar ponto inicial do retângulo")
        print("2 - Alterar largura do retângulo")
        print("3 - Alterar altura do retângulo")
        print("4 - Calcular e mostrar centro do retângulo")
        print("5 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            novo_x = float(input("Digite o novo valor de x para o ponto inicial: "))
            novo_y = float(input("Digite o novo valor de y para o ponto inicial: "))
            ponto_inicial = Ponto(novo_x, novo_y)
            retangulo = Retangulo(ponto_inicial, retangulo.largura, retangulo.altura)
        elif escolha == '2':
            nova_largura = float(input("Digite a nova largura do retângulo: "))
            retangulo = Retangulo(retangulo.ponto_inicial, nova_largura, retangulo.altura)
        elif escolha == '3':
            nova_altura = float(input("Digite a nova altura do retângulo: "))
            retangulo = Retangulo(retangulo.ponto_inicial, retangulo.largura, nova_altura)
        elif escolha == '4':
            centro = retangulo.encontrar_centro()
            centro.imprimir_ponto()
        elif escolha == '5':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
