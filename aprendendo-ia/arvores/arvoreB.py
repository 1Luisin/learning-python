class NoBinario:
    def __init__(self, valor):
        self.valor = valor 
        self.esquerda = None
        self.direita = None

    def inserir_esquerda(self, valor):
        self.esqueda = NoBinario(valor)

    def inserir_direita(self, valor):
        self.direita = NoBinario(valor)