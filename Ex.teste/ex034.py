salario = float(input("Qual o valor do Salario R$ "))

if salario <= 1250.00:
    print("O valor do Salario é R$ {:.2f} e reajustado ficará R$ {:.2f}".format(salario, salario*0.15 + salario))
else:
    print("Ovalor do Salario é R$ {:.2f} e reajustado ficará R$ {:.2f}".format(salario, salario*0.10 + salario))