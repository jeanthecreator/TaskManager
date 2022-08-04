#tabuada

tabuada = int(input("Vamos fazer a tabuada do Numero: "))
i = 1
lista = [1,2,3,4,5,6,7,8,9,10]
print("="*12)
for i in lista:
    print("{} x {:2} = {}".format(tabuada, i, tabuada*i))
print("="*12)