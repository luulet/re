def main():
    while True:
        maara = float(input("Anna bensiinin määrä (gal): "))

        if maara < 0:
            print("Negatiivinen määrä.")
            break
        else: print(f"Tulos: {convertion(maara)}")


def convertion(gallon):
    return gallon * 3.785

main()