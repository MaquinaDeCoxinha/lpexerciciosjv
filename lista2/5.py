opcoes_permitidas = ['1', '2', '3']
class ContaCorrente:
    def __init__(self, numero, nome, saldo=0):
        self.saldo = float(saldo)
        self.numero = numero
        self.nome = nome
    def alterarNome(self, nome):
        self.nome = nome
        self.informacoesConta()
    def deposito(self, deposito):
        self.saldo += float(deposito)
        self.informacoesConta()
    def saque(self, saque):
        self.saldo -= float(saque)
        self.informacoesConta()
    def informacoesConta(self):
        print(f'nome: {self.nome}\nnumero: {self.numero} anos\nsaldo: {self.saldo} R$')

contaCorrente = ContaCorrente(123910, 'Joao', 100)
while True:
    print('Voce deseja:')
    print('1 - Alterar Nome')
    print('2 - Depositar')
    print('3 - Sacar')
    opcao = input()
    if opcao in opcoes_permitidas:
        if opcao == '1':
            nome = input('Qual o nome desejado?')
            contaCorrente.alterarNome(nome=nome)
        elif opcao == '2':
            deposito = input('Quanto deseja depositar?')
            contaCorrente.deposito(deposito=deposito)
        elif opcao == '3':
            saque = input('Quanto deseja sacar?')
            contaCorrente.saque(saque=saque)


