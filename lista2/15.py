class Tamagushi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira
        if self.tedio < 0:
            self.tedio = 0

    def humor(self):
        if self.fome > 70 and self.tedio > 70:
            return "Muito mal-humorado"
        elif self.fome > 70:
            return "Mal-humorado"
        elif self.tedio > 70:
            return "Entediado"
        else:
            return "Feliz"

    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Fome: {self.fome}")
        print(f"Tédio: {self.tedio}")
        print(f"Humor: {self.humor()}")


def main():
    nome_do_bichinho = input("Digite o nome do seu Tamagushi: ")
    bichinho = Tamagushi(nome_do_bichinho)

    while True:
        print("\nOpções:")
        print("1 - Alimentar")
        print("2 - Brincar")
        print("3 - Ver status")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            quantidade_comida = int(input("Quantidade de comida a fornecer: "))
            bichinho.alimentar(quantidade_comida)
        elif opcao == '2':
            tempo_brincadeira = int(input("Tempo de brincadeira (em minutos): "))
            bichinho.brincar(tempo_brincadeira)
        elif opcao == '3':
            bichinho.status()
        elif opcao == '4':
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
