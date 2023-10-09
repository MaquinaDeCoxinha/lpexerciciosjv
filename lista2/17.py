import random

class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 100)
        self.tedio = random.randint(0, 100)

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

def criar_fazenda(num_bichinhos):
    fazenda = []
    for i in range(num_bichinhos):
        nome_bichinho = f"Bichinho {i+1}"
        fazenda.append(Bichinho(nome_bichinho))
    return fazenda

def alimentar_todos(fazenda, quantidade_comida):
    for bichinho in fazenda:
        bichinho.alimentar(quantidade_comida)

def brincar_com_todos(fazenda, tempo_brincadeira):
    for bichinho in fazenda:
        bichinho.brincar(tempo_brincadeira)

def ouvir_todos(fazenda):
    for bichinho in fazenda:
        bichinho.status()

def main():
    num_bichinhos = int(input("Quantos bichinhos você deseja criar na fazenda? "))
    fazenda = criar_fazenda(num_bichinhos)

    while True:
        print("\nOpções:")
        print("1 - Alimentar todos os bichinhos")
        print("2 - Brincar com todos os bichinhos")
        print("3 - Ouvir todos os bichinhos")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            quantidade_comida = int(input("Quantidade de comida a fornecer: "))
            alimentar_todos(fazenda, quantidade_comida)
        elif opcao == '2':
            tempo_brincadeira = int(input("Tempo de brincadeira (em minutos): "))
            brincar_com_todos(fazenda, tempo_brincadeira)
        elif opcao == '3':
            ouvir_todos(fazenda)
        elif opcao == '4':
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
