def main():


    airports = {"00AA": "Aero B Ranch Airport"}
    while True:
        print("Haluatko syöttää uuden lentoaseman (1), hakea lentoaseman tiedot (2) tai lopettaa [Enter]")
        option = input(" > ")
        if option == "1":
            print("Anna lentokentän ICAO-koodi")
            icao = input(" > ")
            print("Anna lentokentän nimi")
            nimi = input(" > ")
            airports.update({icao: nimi})
        elif option == "2":
            print("Anna lentokentän ICAO-koodi")
            icao_search = input(" > ")
            if icao_search in airports:
                print(airports[icao_search])
            else: print("ICAO koodia ei löydetty.")
        elif option == (""):
            print("Näkemiin.")
            break
        else:
            print("Valinta ei '1', '2' tai [enter].")





main()