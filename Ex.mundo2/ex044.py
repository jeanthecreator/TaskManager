print("{:#^40}".format(" Lojas do Futuro "))

vl = float(input("Qual o valor da compra? R$:"))
forma = int(input('''Escolha a forma de pagamento
[ 1 ]  Dinheiro/Cheque
[ 2 ]  Debito/Credito a vista
[ 3 ]  Até 2x no Cartão de credito
[ 4 ]  3x ou mais no Cartão de credito
Opção: '''))

if forma == 1:
    print("O valor da compra ficou R$:{:.2f}, mas terá um desconto e ficará R$:{:.2f}".format(
        vl, vl-(vl*0.10)))
elif forma == 2:
    print("O valor da compra ficou R$:{:.2f}, mas terá um desconto e ficará R$:{:.2f}".format(
        vl, vl-(vl*0.05)))
elif forma == 3:
    print("O valor da compra ficá em 2x de R$:{:.2f} Sem Juros. no Total de R$: {:.2f}".format(
        vl/2, vl))
elif forma == 4:
    parcela = int(input("Quantas parcelas? "))
    print("Sua compra será parcelada em {}x de R$: {:.2f} COM JUROS".format(
        parcela, (vl + (vl*0.20))/parcela))
    print("Sua compra de R$: {:.2f} vai custar R$:{:.2f} no final.".format(
        vl, vl+(vl*0.20)))
else:
    print("Escolha uma opção valida")
