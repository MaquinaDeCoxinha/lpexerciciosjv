class Carro:
    def __init__(self, consumo_km_por_litro):
        self.consumo_km_por_litro = consumo_km_por_litro
        self.nivel_combustivel = 0

    def adicionarGasolina(self, litros):
        self.nivel_combustivel += litros

    def andar(self, distancia):
        combustivel_necessario = distancia / self.consumo_km_por_litro
        if self.nivel_combustivel >= combustivel_necessario:
            self.nivel_combustivel -= combustivel_necessario
        else:
            print("Nível de combustível insuficiente. Abasteça o tanque.")

    def obterGasolina(self):
        return self.nivel_combustivel


meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
print(f"Nível de combustível restante: {meuFusca.obterGasolina()} litros")
