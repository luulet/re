while True:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa!")
        break
    else:
        print()
        print("Pääsy evätty.")
        print()