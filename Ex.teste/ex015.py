#Calculo de Aluguel de carro

dias = int(input("Quantos dias ficou com o carro?: "))
km = float(input("Quantidade de KM rodados: "))
qtdDias = dias * 60
qtdKm = km * 0.15
total = qtdDias + qtdKm

print("Quantidade de dias {}, valor pelos dias R${}, quantidade de KM{}, valor total de KM R${}, total R${}".format(dias, qtdDias, km, qtdKm, total))