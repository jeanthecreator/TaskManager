largura = float(input("Quanto de tinta vc irá precisar, digite o primeiro valor em M2: "))
altura = float(input("Digite o segundo valor: "))
area = largura * altura
tinta = area / 2

print("A quantidade de tinta para uma parede de {} X {},no total de {}M2, vc precisará de {}L de tinta".format(largura, altura, area, tinta))