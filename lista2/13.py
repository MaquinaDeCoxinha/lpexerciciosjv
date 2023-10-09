class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario

funcionario1 = Funcionario("João", 3000.0)
funcionario2 = Funcionario("Maria", 3500.0)

print(f"Nome do funcionário 1: {funcionario1.obter_nome()}")
print(f"Salário do funcionário 1: R${funcionario1.obter_salario():.2f}")

print(f"Nome do funcionário 2: {funcionario2.obter_nome()}")
print(f"Salário do funcionário 2: R${funcionario2.obter_salario():.2f}")
