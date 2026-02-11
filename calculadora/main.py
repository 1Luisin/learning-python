def funcaoPrincipal():
    
    opcaoEscolhida = int(input("Digite qual modo você deseja:" + "\n1 - Soma"+ "\n2 - Subtração"+ "\n3 - Multiplicação"+ "\n4 - Divisão\n"))

    if(opcaoEscolhida == 1):
        funcaoSoma()
    elif(opcaoEscolhida == 2):
        funcaoSubtracao()
    elif(opcaoEscolhida == 3):
        funcaoMultiplicacao()
    elif(opcaoEscolhida == 4):
        funcaoDivisao()
    else:
        print("Opção não encontrada, tente novamente.")
        funcaoPrincipal()

def funcaoSoma():
    input1 = int(input("Digite o primeiro número\n"))
    input2 = int(input("Digite o segundo número\n"))

    resultado = input1 + input2

    print("O resultado da soma entre os dois números é " + str(resultado) + "." )


def funcaoSubtracao():
    input1 = int(input("Digite o primeiro número\n"))
    input2 = int(input("Digite o segundo número\n"))
    
    resultado = input1 - input2

    print("O resultado da soma entre os dois números é " + str(resultado) + "." )

def funcaoMultiplicacao():
    input1 = int(input("Digite o primeiro número\n"))
    input2 = int(input("Digite o segundo número\n"))
    
    resultado = input1 * input2

    print("O resultado da soma entre os dois números é " + str(resultado) + "." )


def funcaoDivisao():
    input1 = int(input("Digite o primeiro número\n"))
    input2 = int(input("Digite o segundo número\n"))
    
    resultado = input1 / input2

    print("O resultado da soma entre os dois números é " + str(resultado) + "." )


funcaoPrincipal()

