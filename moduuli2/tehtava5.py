leivi_str = input("Anna leiviskät: ")
naula_str = input("Anna naulat: ")
luoti_str = input("Anna luodit: ")
leivi = int(leivi_str) * 8.512
naula = int(naula_str) * 0.4256
luoti = int(luoti_str) * 0.0133
# leivi on 8512 grammaa ja naula on 425,6 grammaa
vastauskg = (leivi + naula + luoti)
vastausg = ((leivi + naula + luoti) - int(vastauskg)) * 1000


print("Massa nykymittojen mukaan: ")
print(str(int(vastauskg)) + " kilogrammaa ja " + str(vastausg) + " grammaa.")

