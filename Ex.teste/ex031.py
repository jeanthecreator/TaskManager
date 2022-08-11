print("Vamos calcular o preço da sua passagem")
km = float(input("Quantos km seu onibus irá percorrer?: "))

if km <= 200:
    print("Sua passagem irá custar 0,50 por Km total de R${}".format(km * 0.50))
else:
    print("Sua passagem irá custar 0,45 por Km total de R${}".format(km * 0.45))