def busca (v, chave): #v = lista / chave = valor a ser buscado
    i = 0 #contador

    while i < len(v) and chave != v[i]: # se o contador for menor que a lista e diferente do valor que procuramos. . .
        i = i + 1 #. . .continue a contagem
 
    if i < len(v) and chave == v[i]: # se o contador for menor que a lista mas igual ao valor que procuramos. . .
        return i #. . .pare e me dê o valor. . .
    else:   # ...ou...
        return "O número não se encontra dentro da lista." #... me retorne um texto dizendo que nao encontrou
 

array = [0,1,2,3,4,5]
chave = 4
print(busca(array,chave))
