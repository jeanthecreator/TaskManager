#Conversor de medidas

medida = float(input("Conversor de medidas, Digite em metros: "))

print("A Medida de {} metros, corresponde á {}KM ".format(medida, medida / 1000))
print("{}hm".format(medida / 100))
print("{}dam".format(medida / 10))
print("{}dm".format(medida * 10))
print("{}cm".format(medida * 100))
print("{}mm".format(medida * 1000))