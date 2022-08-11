from itertools import count
from re import U


frase = str(input("Digite uma frase: ")).strip()

conta = frase.lower().count('a')
achar = frase.lower().find('a')+1
ult = frase.lower().rfind('a')+1
print(conta)
print(achar)
print(ult)