import random

kone = random.randint(1,10)


while True:
    kayttaja = int(input("Anna luku väliltä 1..10: "))
    if kone > kayttaja:
        print("Liian pieni arvaus.")
    if kone < kayttaja:
        print("Liian suuri arvaus.")
    if kone == kayttaja:
        print("Oikein!")
        break
