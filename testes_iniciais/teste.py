

fruta1, fruta2, fruta3 = "banana","maça","mexerica"

frutas = ["coco", "abacate", "mamão"]
print(fruta1, fruta2, fruta3)
print(frutas)

number = 5 
number2 = 2


if number > number2: 
        print ("5 é maior que 2", end=" ") #end na linguagem serve para fazer com que o proximo texto fique na mesma linha
        print("teste de outro texto")
        print(type(number)) # type é uma função que mostra o tipo de um objeto
        print(type(fruta1), type(fruta2))

    
elif number == number2:
        print("shit2")

else:
        print("shit!")



acoes = ["andar", "correr", "caminhar"]

x, y, z = acoes #unpacking 

print (x,y,z)