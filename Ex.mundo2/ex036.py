print("*="*35)
print("Vamos calcular se você poderá fazer o emprestimos para essa casa")
print("*="*35)
vCasa =float(input("Qual o valor da casa? R$: "))
aPaga =float(input("Em quantos anos você pretende pagar?: "))
mSala =float(input("Qual o seu Salario Mensal?: "))

valida = mSala * 0.30
pAno = aPaga * 12
print(valida)
if vCasa / pAno > valida:
    print("Imprestimo Negado, o valor da parecela tem que ser menor que R$:{:.2f} e o valor total da parcela esta R$:{:.2f}".format(valida,vCasa/pAno ))
elif vCasa / pAno < valida:
    print("Emprestino aprovado, o valor da parcela será de R$: {:.2f}".format(vCasa/pAno))
else:
    print("Emprrestimo aprovado, mas esta muito com o valor no limite, a parcela ficará R$: {}".format(vCasa/pAno))