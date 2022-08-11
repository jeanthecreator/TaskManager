from posixpath import split


nome = str(input("Digite o seu nome completo: "))
sp = nome.split()
n = nome.replace(" ", "")
print("Seu nome Maiusculo", nome.upper())
print("Seu nome minusculo", nome.lower())
print("Seu nome tem um tamanho de {} caracteres sem espaços ".format(len(n)))
print("O seu primeiro nome é:", sp[0])
print("Seu primeiro nome tem o tamanho de: ", len(sp[0]))

