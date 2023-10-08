opcoes_permitidas = ['1', '2', '3', '4']
class Retangulo:
    def __init__(self, base, altura):
        self.altura = int(altura)
        self.base = int(base)
    def trocaLado(self, base, altura):
        self.altura = int(altura)
        self.base = int(base)
        print(f'tamanho da base trocado para {self.base} com sucesso!')
        print(f'tamanho da altura trocado para {self.altura} com sucesso!')
    def mostraTamanhoLado(self):
        return f'base:{self.base} altura:{self.altura}'
    def calcularArea(self):
        self.area = self.altura*self.base
        return self.area
    def calcularPerimetro(self):
        self.perimetro = (self.altura*2)+(self.base*2)
        return self.perimetro

retangulo = Retangulo(30,10)
while True:
    print('Voce deseja:')
    print('1 - Trocar tamanho dos lados')
    print('2 - Mostrar tamanho dos lados')
    print('3 - Calcular Area')
    print('4 - Calcular Perimetro')
    opcao = input()
    if opcao in opcoes_permitidas:
        if opcao == '1':
            base = input('Qual o tamanho da base desejada?')
            altura = input('Qual o tamanho da altura desejada?')
            retangulo.trocaLado(base=base,altura=altura)
        elif opcao == '2':
            print(retangulo.mostraTamanhoLado())
        elif opcao == '3':
            print(retangulo.calcularArea())
        elif opcao == '4':
            print(retangulo.calcularPerimetro())


