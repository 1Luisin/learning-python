class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

    def adicionar_filho(self, no_filho):
        self.filhos.append(no_filho)

    def mostrar_arvore(self, nivel=0):
        prefixo = "    " * nivel + "_ _ _" if nivel > 0 else ""
        print(prefixo + str(self.valor))

        for filho in self.filhos:
            filho.mostrar_arvore(nivel + 1)


diretor = NoArvore("Diretor (CEO)")
gerente_ti = NoArvore("Gerente TI")
gerente_vendas = NoArvore("Gerente Vendas")

dev_front = NoArvore("Desenvolvedor Front-end")
dev_back = NoArvore("Desenvolvedor back_end")
vendedor_1 = NoArvore("vendedor externo")

diretor.adicionar_filho(gerente_ti)
diretor.adicionar_filho(gerente_vendas)

gerente_ti.adicionar_filho(dev_back)
gerente_ti.adicionar_filho(dev_front)

gerente_vendas.adicionar_filho(vendedor_1)

diretor.mostrar_arvore()
