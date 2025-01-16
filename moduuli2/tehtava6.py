import random
print("Kolminumeroinen koodi, jonka kukin numeromerkki on väliltä 0-9.")
print(random.randint(0, 999))
eka = random.randint(0, 6)
toka = random.randint(0, 6)
kolmas = random.randint(0, 6)
nelj = random.randint(0, 6)
print("Nelinumeroinen koodi, jonka kukin numeromerkki on väliltä 0-6.")
print(f"{eka}{toka}{kolmas}{nelj}")

