import os

def clearConsole():
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

clearConsole()
print("tela limpa!")