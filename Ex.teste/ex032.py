print("Vamos verificar se o ano é Bissexto!!")
ano = int(input("Digite o ano: "))
veri = ano%4

if veri == 0:
    print("Ano Bissexto!!")
else:
    print("Ano não Bissexto!!")