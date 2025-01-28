hit = False
num = int(input("Anna kokonaisluku: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            hit = True
            break

if hit:
    print(num, "ei ole alkuluku")
else:
    print(num, "on alkuluku")