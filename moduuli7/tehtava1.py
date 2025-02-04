def main():

    while True:
        vuodenajat = ("talvi","talvi","kevät","kevät","kevät","kesä","kesä","kesä","syksy","syksy","syksy","talvi")
        numero = int(input("Anna kuukauden järjestysnumero (1/12): "))
        vuodenaika = (vuodenajat[numero-1])
        if 1 <= numero <= 12:
            print(f"{numero}. kuukauden vuodenaika on {vuodenaika}.")
        else:
             break




main()