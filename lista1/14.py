def isfloat(string):   #declarando função de verificação utilizada no código
    try:
        float(string)
        return True
    except ValueError:
        return False

class Program:  #declarando a classe em que o programa funciona

    def __init__(self):
            self.tara = 50  #limite do peso (em quilos) que pode ser pescado
            self.taxa = 4   #quanto deve ser pago(em reais) por quilo de peixe em excesso
            self.peso = self.obter_peso()   #Obtém a altura em float

    def obter_peso(self):
        getting_input = True    #variável de controle 
        while getting_input:    #enquanto o programa estiver coletando informações
            peso = input("Digite quanto quilos de peixe foram coletados por José ")   #coleta o input do usuário e verifica se é um inteiro tentando converte-lo de string para inteiro
            if(isfloat(peso)):     #verifica se o input é um numero real
                getting_input = False   #se o input for um numero real, termina o loop de input
            else:
                print("o numero inserido não é válido, por favor tente novamente")
                continue    #se o numero não for válido, avisa o usuário e continua o loop de input 
        return float(peso)     #retorna o número já convertido como uma variável do objeto Program
    
    def calcular(self):
        if (self.peso > 50):
            self.excesso = self.peso - self.tara    #calcula o quanto (em quilos) a mais foi pego
            self.multa = self.excesso * self.taxa   #calcula o quanto (em reais) deve ser pago por José
            print(f'José pegou {self.excesso:.2f}kg a mais que o limite! Ele deve pagar R${self.multa:.2f}!')
        else:
            print(f'José pegou {(self.tara - self.peso):.2f}kg a menos que a tara! Não precisará pagar multa.')


main = Program()
main.calcular()