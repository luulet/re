import math
from random import uniform
print("Ohjelma laskee piin likiarvon annettujen toistojen perusteella.")
kerrat = int(input("Anna toistojen määrä: "))
tehdyt = 0
sisa = 0
ulko = 0
while tehdyt < kerrat:
    tehdyt = tehdyt + 1
    y = uniform(-1,1)
    x = uniform(-1,1)
    if pow(x, 2) + pow(y, 2) < 1:
        sisa = sisa + 1
print("Piin likiarvo: ", ((4*sisa)/kerrat), ".", sep="")