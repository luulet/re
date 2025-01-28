import random
arvat =[]

arpa = int(input("Anna arpojen määrä: "))

for _ in range(arpa):
    heitto = random.randint(1,6)
    arvat.append(int(heitto))
print("Heittojen summa on " + str(sum(arvat)) + ".")


