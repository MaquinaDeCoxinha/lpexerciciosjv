opcoes_permitidas = ['1', '2', '3']
class Quadrado:
    def __init__(self, lado):
        self.tamanho_lado = lado
    def trocaLado(self, lado):
        self.tamanho_lado = lado
        print(f'tamanho do lado trocado para {self.tamanho_lado} com sucesso!')
    def mostraTamanhoLado(self):
        return self.tamanho_lado
    def calcularArea(self):
        self.area = float(self.tamanho_lado)**2
        return self.area

quadrado = Quadrado(30)
while True:
    print('Voce deseja:')
    print('1 - Trocar tamanho do lado')
    print('2 - Mostrar tamanho do lado')
    print('3 - Calcular Area')
    opcao = input()
    if opcao in opcoes_permitidas:
        if opcao == '1':
            lado = input('Qual o tamanho do lado desejado?')
            quadrado.trocaLado(lado)
        elif opcao == '2':
            print(quadrado.mostraTamanhoLado())
        elif opcao == '3':
            print(quadrado.calcularArea())


