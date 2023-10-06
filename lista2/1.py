opcoes_permitidas = ['1', '2']
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        self.metodos = [self.trocaCor, self.mostraCor]
    def trocaCor(self, cor):
        self.cor = cor
        print(f'cor trocada para {self.cor} com sucesso!')
    def mostraCor(self):
        print(f'{self.cor}')

bola = Bola('verde', 30, 'borracha')
while True:
    print('Voce deseja:')
    print('1 - Trocar Cor')
    print('2 - Mostrar Cor')
    opcao = input()
    if opcao in opcoes_permitidas:
        if opcao == '1':
            cor_desejada = input('Qual cor você deseja?')
            bola.trocaCor(cor_desejada)
        elif opcao == '2':
            bola.mostraCor

