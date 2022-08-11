frase = str(input("Digite seu nome completo: ")).strip().lower()
separada = frase.split()

print("Seu primeiro nome é: {}".format(separada[0]))
print("Seu ultimo nome é: {}".format(separada[len(separada)-1]))