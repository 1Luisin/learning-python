# Questão 1) Faça um procedimento que receba por parâmetro um número inteiro e escreva “par” se o número recebido por parâmetro for par. Caso contrário, o procedimento deve escrever “ímpar”. No método principal (Main), leia um número inteiro e passe-o por parâmetro para o procedimento criado.

par = 0
ímpar = 1

def procedimento(numeroInteiro):
    if(numeroInteiro % 2 == 0):
        print(par)
    else:
        print(ímpar)

def Main():
    numberInput = int(input("Escreva um número inteiro"))
    procedimento(numberInput)

Main()
