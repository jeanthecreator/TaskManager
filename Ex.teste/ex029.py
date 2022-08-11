print("Vamos Analisar se voce foi multado Nessa Rodovia")
velo = float(input("Qual a velocidade que voce estava?: "))

if velo > 80:
    print("Voce foi multado em: R${:.2f}".format((velo - 80)* 7))
else:
    print("Parabens voce seguiu o limite da Via")