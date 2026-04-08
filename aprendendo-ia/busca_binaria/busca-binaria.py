
# método de busca binária, 
def busca_binaria(v, chave): # V é a lista de objetos e chave é o objeto que estamos procurando
    
    esq = 0 # esq = 0: Você coloca o dedo da mão esquerda na primeira caixa (índice 0).
   
    dir = len(v) - 1 # Por que len(v) - 1? Se a lista tem 10 itens, o len é 10. Mas lembra que a contagem começa no 0? Então os índices vão de 0 a 9.
    
    pos = (esq +  dir) // 2 #A variável pos é o cálculo de qual caixa está exatamente no meio dos seus dois dedos (esq e dir
    
    while esq <= dir and chave != v[pos]:
        if chave < v[pos]: # o alvo é menor que o valor do meio?
            dir = pos - 1 # então 
        else: 
            esq = pos + 1
        pos = (esq + dir) // 2

    return pos if esq <= dir else -1

# Exemplo de uso:
array = [1, 3, 5, 7, 9]
chave = 3
print(busca_binaria(array, chave))  # Saída: 2