class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return f"Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}."
        else:
            return "Quantidade de combustível insuficiente na bomba."

    def abastecer_por_litro(self, litros):
        valor_a_pagar = litros * self.valor_litro
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
            return f"Valor a pagar: R${valor_a_pagar:.2f}."
        else:
            return "Quantidade de combustível insuficiente na bomba."

    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade_combustivel):
        self.quantidade_combustivel = nova_quantidade_combustivel


def main():
    print("Programa da Bomba de Combustível")

    tipo_combustivel = input("Informe o tipo de combustível: ")
    valor_litro = float(input("Informe o valor do litro de combustível: "))
    quantidade_combustivel = float(input("Informe a quantidade de combustível na bomba (em litros): "))

    bomba = BombaCombustivel(tipo_combustivel, valor_litro, quantidade_combustivel)

    while True:
        print("\nMenu:")
        print("1 - Abastecer por valor")
        print("2 - Abastecer por litro")
        print("3 - Alterar valor do litro")
        print("4 - Alterar tipo de combustível")
        print("5 - Alterar quantidade de combustível na bomba")
        print("6 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            valor_abastecido = float(input("Informe o valor a ser abastecido: "))
            resultado = bomba.abastecer_por_valor(valor_abastecido)
            print(resultado)
        elif escolha == '2':
            litros_abastecidos = float(input("Informe a quantidade em litros a ser abastecida: "))
            resultado = bomba.abastecer_por_litro(litros_abastecidos)
            print(resultado)
        elif escolha == '3':
            novo_valor_litro = float(input("Informe o novo valor do litro de combustível: "))
            bomba.alterar_valor(novo_valor_litro)
        elif escolha == '4':
            novo_tipo_combustivel = input("Informe o novo tipo de combustível: ")
            bomba.alterar_combustivel(novo_tipo_combustivel)
        elif escolha == '5':
            nova_quantidade_combustivel = float(input("Informe a nova quantidade de combustível na bomba (em litros): "))
            bomba.alterar_quantidade_combustivel(nova_quantidade_combustivel)
        elif escolha == '6':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
