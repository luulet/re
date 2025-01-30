def main():
    print("Anna listaan kokonaislukuja, ja ohjelma karsii parittomat luvut.")
    print("Paina Enter kun kaikku luvut on annettu.")


    lista = []
    kokonaisluku = input(" > ")
    while kokonaisluku != (""):
        lista.append(int(kokonaisluku))
        kokonaisluku = input(" > ")
    print(f"Kokonaisluvut: {lista} ")
    print(f"Parilliset kokonaisluvut {kars(lista)}")


def kars(lista):
    for i in lista:
        if i % 2 == 0:
            pass
        else:
            lista.remove(i)
    return lista

main()