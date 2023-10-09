class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def ver_bucho(self):
        if self.bucho:
            print(f"{self.nome} está com o seguinte conteúdo no estômago:")
            for alimento in self.bucho:
                print(f"- {alimento}")
        else:
            print(f"{self.nome} está com o estômago vazio.")

    def digerir(self):
        if self.bucho:
            print(f"{self.nome} está digerindo a comida.")
            self.bucho = []
        else:
            print(f"{self.nome} não pode digerir porque o estômago está vazio.")

macaco1 = Macaco("Macaco A")
macaco2 = Macaco("Macaco B")

macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco2.comer("Peixe")

macaco1.ver_bucho()
macaco2.ver_bucho()

macaco1.digerir()
macaco2.digerir()

print(f"Tentando fazer {macaco1.nome} comer {macaco2.nome}...")
macaco1.comer(macaco2)

macaco1.ver_bucho()
macaco2.ver_bucho()
