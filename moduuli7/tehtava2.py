def main():
    hit = True

    nimet = {}
    nimet = set()

    print("Luettele nimiä ja jatkaaksesi paina Enter.")
    while hit:

        user_input = input(" > ")


        if user_input not in nimet:
            if user_input != (""):
                nimet.add(user_input)
                print("Uusi nimi")

        elif user_input in nimet:
            print("Aiemmin syötetty nimi")

        if user_input == (""):
                hit = False

    for nimi in nimet:
        print(nimi, end=", ")

main()

