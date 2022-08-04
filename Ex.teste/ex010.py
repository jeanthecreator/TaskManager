#Coversor de moeda

moeda = float(input("Conversor de moeda, Quanto vc quer converter do Real?: "))

print("Com R${}, vc pode comprar ${:.2f} dolares e {:.2f} Euros".format(moeda, moeda/5.4, moeda/6.3))