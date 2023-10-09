class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100

    def adicione_juros(self):
        self.saldo += self.saldo * self.taxa_juros

    def consultar_saldo(self):
        return self.saldo

minha_conta = ContaInvestimento(1000.00, 10.0)

for _ in range(5):
    minha_conta.adicione_juros()

saldo_resultante = minha_conta.consultar_saldo()
print(f"Saldo resultante após cinco aplicações de juros: R${saldo_resultante:.2f}")
