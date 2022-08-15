print("*-"*18)
print("Classificação do tipo do triangulo!!")
print("*-"*18)

n1 = float(input("Primeiro segmento: "))
n2 = float(input("Segundo segmento: "))
n3 = float(input("Terceiro segmento: "))

modulo = abs(n1 - n2)

if modulo < n3 < (n1 + n2) and n1 == n2 == n3:
    print("Triangulo Equilátero")
elif modulo < n3 < (n1 + n2) and n1 == n2 or n1 == n3 or n2 == n3:
    print("Triagulo Isósceles")
elif modulo < n3 < (n1 + n2):
    print("Triagulo Escaleno")
else:
    print("Não é um Triangulo")
