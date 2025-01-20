print("Selvitetään onko annettu vuosiluku karkausvuosi vai ei.")
vuosi = float(input("Anna vuosiluku: "))
jako = float(vuosi%4 == 0)
if (vuosi==jako):
    print("joo")
else:
    print("häh")

