kanta_str = input("Anna suorakulman kanta: ")
korkeus_str = input("Anna suorakulman korkeus: ")
kanta = int(kanta_str)
korkeus = int(korkeus_str)
piiri = (kanta * 2) + (korkeus * 2)
pinta = kanta * korkeus
print("Suorakulmion piiri on " + str(piiri) + ".")
print("Suorakulmion pinta-ala on " + str(pinta) + ".")
