print("Ohjelma muuntaa tuumat senttimetreiksi. Negatiivinen lukumäärä lopettaa ohjelman.")
tuuma = float(input("Anna tuumat: "))
while tuuma >= 0:
    print(f"Annetut tuumat ovat {tuuma*2.54}.")
    tuuma = float(input("Anna tuumat: "))
else:
    print("Negatiivinen lukumäärä, näkemiin.")