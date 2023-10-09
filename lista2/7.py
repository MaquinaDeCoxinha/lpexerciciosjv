class Tamagushi:
    def __init__(self, nome, fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = float(fome)
        self.saude = float(saude)
        self.idade = idade

    def alterar_nome(self, nome):
        self.nome = nome
        self.informacoes_tamagushi()

    def alterar_fome(self, fome):
        self.fome = float(fome)
        self.informacoes_tamagushi()

    def alterar_saude(self, saude):
        self.saude = float(saude)
        self.informacoes_tamagushi()

    def alterar_idade(self, idade):
        self.idade = idade
        self.informacoes_tamagushi()

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def calcular_humor(self):
        humor = (self.saude + 100 - self.fome) / 2
        return humor

    def informacoes_tamagushi(self):
        print(f'Nome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade}\nHumor: {self.calcular_humor()}')

tamagushi = Tamagushi("Tama", fome=50, saude=80, idade=2)

while True:
    print('O que deseja fazer com o Tamagushi?')
    print('1 - Alterar Nome')
    print('2 - Alterar Fome')
    print('3 - Alterar Saúde')
    print('4 - Alterar Idade')
    print('5 - Mostrar informações')
    print('6 - Sair')
    opcao = input()

    if opcao == '1':
        nome = input('Digite o novo nome: ')
        tamagushi.alterar_nome(nome)
    elif opcao == '2':
        fome = input('Digite o nível de fome: ')
        tamagushi.alterar_fome(fome)
    elif opcao == '3':
        saude = input('Digite o nível de saúde: ')
        tamagushi.alterar_saude(saude)
    elif opcao == '4':
        idade = input('Digite a nova idade: ')
        tamagushi.alterar_idade(idade)
    elif opcao == '5':
        tamagushi.informacoes_tamagushi()
    elif opcao == '6':
        print('Saindo do programa.')
        break
    else:
        print('Opção inválida. Tente novamente.')
