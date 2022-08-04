produto = float(input("Qual o valor do produto: "))
comDesconto = produto - (produto * 0.05)

print("O valor do produto é de R${} com o desconto de 5% fica por R${:.2f}".format(produto, comDesconto))