def main():
    while True:
        result = noppa()
        print(result)
        if result == 6:
            break
        else:
            pass
def noppa():
    import random
    return random.randint(1,6)

main()