import math

ang = int(input("Digite o Angulo: "))

rad = math.radians(ang)
print("O angulo de {}°, Tem o Seno de {:.2f}".format(ang, math.sin(rad)))
print("O angulo de {}°, Tem o Cosseno de {:.2f}".format(ang, math.cos(rad)))
print("O angulo de {}°, Tem a Tangente de {:.2f}".format(ang, math.tan(rad)))
