opcoes_permitidas = ['1', '2', '3', '4']
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = int(idade)
        self.altura = float(altura)
        self.peso = float(peso)
    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.altura += 0.005
        self.mostrarAtributos()
    def engordar(self, peso):
        self.peso += float(peso)
        self.mostrarAtributos()
    def emagrecer(self, peso):
        self.peso -= float(peso)
        self.mostrarAtributos()
    def crescer(self, altura):
        self.altura += float(altura)
        self.mostrarAtributos()
    def mostrarAtributos(self):
        print(f'nome: {self.nome}\nidade: {self.idade} anos\naltura: {self.altura}m\npeso: {self.peso}kg')

pessoa = Pessoa('Joao', 15, 65.25, 1.55)
while True:
    print('Voce deseja:')
    print('1 - Envelhecer')
    print('2 - Engordar')
    print('3 - Emagrecer')
    print('4 - Crescer')
    opcao = input()
    if opcao in opcoes_permitidas:
        if opcao == '1':
            pessoa.envelhecer()      
        elif opcao == '2':
            peso = input('Qual o aumento de peso?')
            pessoa.engordar(peso=peso)
        elif opcao == '3':
            peso = input('Qual o decrescimo de peso?')
            pessoa.emagrecer(peso=peso)
        elif opcao == '4':
            altura = input('Qual o aumento de altura?')
            pessoa.crescer(altura=altura)


