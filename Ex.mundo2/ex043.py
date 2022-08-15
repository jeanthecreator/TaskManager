print("*-"*8)
print("Calculadora IMC")
print("*-"*8)

peso = float(input("Digite o seu peso atual: "))
altu = float(input("Digite a sua Altura: "))

imc = peso / altu ** 2

print(imc)
if imc <= 18.5:
    print("Abaixo do peso: Classificação Magreza")
elif imc > 18.5 and imc < 25:
    print("Peso ideal: Classificação Normal")
elif imc >= 25 and imc < 30:
    print("Acima do peso: Classificação Sobrepeso")
elif imc > 30 and imc < 40:
    print("Classificação Obesidade")
else:
    print("Classificação obesidade grave!!")
