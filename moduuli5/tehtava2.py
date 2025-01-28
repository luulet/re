luvut = []

luku = input("Anna luku tai lopeta painamalla Enter: ")
while luku != "":
    luvut.append(int(luku))
    luku = input("Anna luku tai lopeta painamalla Enter: ")

luvut.sort(reverse=True)
print(luvut[0:5])
