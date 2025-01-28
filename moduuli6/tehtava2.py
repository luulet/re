def main():
    silma = int(input("Anna nopan silmäluku: "))
    while True:
        result = noppa(silma)
        print(result)
        if result == silma:
            break
        else:
            pass

def noppa(silma):
    import random
    return random.randint(1,silma)



main()