from sre_compile import isstring


digite = input("Digite algo: ")
print("Tipo", type(digite))
print("Numero? ", digite.isnumeric())
print("Alpha? ", digite.isalpha())
print("Maiuscula? ", digite.isupper())
print("Minuscula? ", digite.islower())
print("Capitalizada? ", digite.istitle())

print("Tipo{}\nNumero{}\n".format(type(digite), digite.isnumeric()))
