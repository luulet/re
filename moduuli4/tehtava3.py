print("Voit antaa lukuja siihen saakka, kunnes syötät tyhjän merkkijonon.")
lista = []
while True:
    luku = (input("Anna luku: "))
    if luku == "":
        break
    lista.append(int(luku))
print(f"Annetuista luvuista pienin on {min(lista)} ja suurin on {max(lista)}.")