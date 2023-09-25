def isfloat(string):   #declarando função de verificação utilizada no código
    try:
        float(string)
        return True
    except ValueError:
        return False


class Program:  #declarando a classe em que o programa funciona

    def __init__(self):
            self.num1 = self.obter_num1()   #Obtém o primeiro número
            self.num2 = self.obter_num2()   #Obtém o segundo número
            self.num3 = self.obter_num3()   #Obtém o terceiro número

    def obter_num1(self):
        getting_input = True    #variável de controle 
        while getting_input:    #enquanto o programa estiver coletando informações
            try:
                num1 = int(input("Digite o primeiro numero inteiro "))   #coleta o input do usuário e verifica se é um inteiro tentando converte-lo de string para inteiro
            except:
                print("o numero inserido não é válido, por favor tente novamente")
                continue    #se o numero não for válido, avisa o usuário e continua o loop de input
            getting_input = False   #se a conversão der certo, termina o loop de input
        return num1     #retorna o número já convertido como uma variável do objeto Program
    
    def obter_num2(self):
        getting_input = True    #variável de controle 
        while getting_input:    #enquanto o programa estiver coletando informações
            try:
                num2 = int(input("Digite o segundo numero inteiro "))   #coleta o input do usuário e verifica se é um inteiro tentando converte-lo de string para inteiro
            except:
                print("o numero inserido não é válido, por favor tente novamente")
                continue    #se o numero não for válido, avisa o usuário e continua o loop de input
            getting_input = False   #se a conversão der certo, termina o loop de input
        return num2     #retorna o número já convertido como uma variável do objeto Program
    
    def obter_num3(self):
        getting_input = True    #variável de controle 
        while getting_input:    #enquanto o programa estiver coletando informações
            num3 = input("Agora digite um numero real ")   #coleta o input do usuário e verifica se é um inteiro tentando converte-lo de string para inteiro
            if(isfloat(num3)):     #verifica se o input é um numero real
                getting_input = False   #se o input for um numero real, termina o loop de input
            else:
                print("o numero inserido não é válido, por favor tente novamente")
                continue    #se o numero não for válido, avisa o usuário e continua o loop de input 
        return float(num3)     #retorna o número já convertido como uma variável do objeto Program

    def calcular(self):
        self.resultado_a =  2*(self.num1) + (self.num2)/2
        self.resultado_b =  3*(self.num1) + self.num3
        self.resultado_c =  (self.num3)**3
        print(f'O produto do dobro do primeiro({self.num1}) com metade do segundo({self.num2}) = {self.resultado_a}')
        print(f'A soma do triplo do primeiro({self.num1}) com o terceiro({self.num3}) = {self.resultado_b}')
        print(f'O terceiro({self.num3}) elevado ao cubo = {self.resultado_c}')


main = Program()
main.calcular()