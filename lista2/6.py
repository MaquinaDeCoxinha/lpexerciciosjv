class Televisor:
    def __init__(self):
        self.canal_atual = 1
        self.volume = 10

    def alterar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal_atual = novo_canal
            print(f"Canal atual: {self.canal_atual}")
        else:
            print("Canal inválido. Use um número de canal entre 1 e 100.")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume atual: {self.volume}")
        else:
            print("Volume máximo atingido.")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume atual: {self.volume}")
        else:
            print("Volume mínimo atingido.")

televisor = Televisor()

while True:
    print("O que deseja fazer?")
    print("1 - Alterar canal")
    print("2 - Aumentar volume")
    print("3 - Diminuir volume")
    print("4 - Desligar o televisor")
    opcao = input()

    if opcao == "1":
        novo_canal = int(input("Digite o número do canal desejado: "))
        televisor.alterar_canal(novo_canal)
    elif opcao == "2":
        televisor.aumentar_volume()
    elif opcao == "3":
        televisor.diminuir_volume()
    elif opcao == "4":
        print("Televisor desligado.")
        break
    else:
        print("Opção inválida. Escolha uma das opções disponíveis.")
