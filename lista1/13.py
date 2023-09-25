def isfloat(string):   #declarando função de verificação utilizada no código
    try:
        float(string)
        return True
    except ValueError:
        return False


class Program:  #declarando a classe em que o programa funciona

    def __init__(self):
            self.sexos_permitidos = ["masculino","feminino"]
            self.altura = self.obter_altura()   #Obtém a altura
            self.sexo = self.obter_sexo()     #Obtém o sexo do indivíduo

    def obter_altura(self):
        getting_input = True    #variável de controle 
        while getting_input:    #enquanto o programa estiver coletando informações
            altura = input("Digite uma altura em metros ")   #coleta o input do usuário e verifica se é um inteiro tentando converte-lo de string para inteiro
            if(isfloat(altura)):     #verifica se o input é um numero real
                getting_input = False   #se o input for um numero real, termina o loop de input
            else:
                print("o numero inserido não é válido, por favor tente novamente")
                continue    #se o numero não for válido, avisa o usuário e continua o loop de input 
        return float(altura)     #retorna o número já convertido como uma variável do objeto Program
    
    def obter_sexo(self):
        getting_input = True    #variável de controle 
        while getting_input:    #enquanto o programa estiver coletando informações
            sexo = input("Digite o sexo biológico do individuo(masculino ou feminino) ")   #coleta o input em string do usuário
            if(sexo in self.sexos_permitidos):     #verifica se o input um sexo válido dentro da lista declarada no construtor
                getting_input = False   #se o input for um válido, termina o loop de input
            else:
                print("o numero inserido não é válido, por favor tente novamente")
                continue    #se o input não for válido, avisa o usuário e continua o loop de input 
        return sexo     #retorna o sexo do indivíduo como uma variável do objeto Program

    def calcular(self):
        if (self.sexo == "masculino"):  #caso seja do sexo masculino
            self.peso_ideal =  (self.altura*72.7) - 58
        else:   #caso seja do sexo feminino
            self.peso_ideal =  (self.altura*62.1) - 44.7
        print(f'O peso ideal desse individuo é: {self.peso_ideal:.2f}kg')

main = Program()
main.calcular()